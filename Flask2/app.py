
from database import Database
from flask import Flask, request, render_template, g, redirect

app = Flask(__name__)

# L'objet global g nous permet de gérer les ressources pendant une requete

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
    
@app.route("/personnes")
def personnes():
  personnes = get_db().get_all_persons()
  return render_template("personnes.html", personnes=personnes)



@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'GET':
    return render_template("home.html")
  else:
    nom = request.form["nom"]
    prenom = request.form["prenom"]
    age = request.form["age"]
    
    if nom == "" or prenom == "" or age == "":
      return render_template("home.html", error="Tous les champs sont obligatoires!")
    else:
      get_db().add_person(nom, prenom, age)
      return redirect("/personnes")