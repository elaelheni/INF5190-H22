import re
from database import Database
from datetime import date
from flask_bcrypt import Bcrypt
from flask import Flask, g, render_template, request, flash, redirect

app = Flask(__name__)

# Généré avec : import secrets, secrets.token_hex(16)
app.config['SECRET_KEY'] = '6037c42d03efa5aefc117a302260bcb7'

bcrypt = Bcrypt(app)

def get_db():
  # Créer une ressource si cette dernière n'existe pas
  db = getattr(g, '_database', None)
  if db is None:
    g._database = Database()
  return g._database

# Fermer/ Désaloueer la ressource si elle existe
@app.teardown_appcontext
def close_connection(exception):
  db = getattr(g, '_database', None)
  if db is not None:
    db.disconnect()
    
regex = r'[A-Za-z0-9#@%]{8,}'
match_mdp = re.compile(regex).match
  
def validate_mdp(str):
  try:
    if match_mdp(str) is not None:
      return True
  except:
    pass
  return False
  
def courriel_existe(courriel):
  return get_db().mail_exists(courriel)

def validate_courriel(courriel, validation_courriel):
  return courriel == validation_courriel

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'GET':
    return render_template('home.html')
  else:
    nom = request.form['nom']
    courriel = request.form['courriel']
    validation_courriel = request.form['validation-courriel']
    mdp = request.form['mdp']
    if nom == "" or courriel == "" or validation_courriel == "" or mdp == "":
      flash('ERREUR! Tous les champs sont obligatoires', category='error')
      return render_template('home.html')
    if courriel_existe(courriel):
      return render_template('home.html', mail_error="L'adresse courriel est déjà utilisée")
    if validate_courriel(courriel, validation_courriel) is False:
      return render_template('home.html', mail_error="Attention les deux adresses courriels sont différentes")
    if validate_mdp(mdp) is False:
      return render_template('home.html', mdp_error="Le mot de passe est du mauvais format")
    
    hashed_password = bcrypt.generate_password_hash(mdp).decode('utf-8')
    date_inscription = date.today()
    get_db().insert_user(nom, courriel,date_inscription, hashed_password)
    flash('Félicitations vous etes inscrits', 'success')
    return redirect ('/confirmation')
  
@app.route('/confirmation')
def confirmation():
  return render_template('confirmation.html')
    



