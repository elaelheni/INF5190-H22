from flask import Flask, render_template, request, redirect, flash, url_for
from flask_bcrypt import Bcrypt
from shared import db
from database import User
from flask_mail import Mail, Message
from flask_login import LoginManager, login_user, logout_user
from forms import Inscription, Login
from itsdangerous import URLSafeTimedSerializer


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'

app.config['SECRET_KEY'] = 'fd1827619e167626fb0032ea8e922323'
app.config['SECURITY_PASSWORD_SALT'] = '60ccf3a7956ba3bbf5b3f3b6f8990ee9'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'steeve.inf5190@gmail.com'
app.config['MAIL_PASSWORD'] = 'Secret123.'

db.init_app(app)
mail = Mail(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

with app.app_context():
  db.create_all()
 
# Le callback user_loader est utilisé pour recharger l'objet utilisateur à partir de l'ID utilisateur
# stocké dans la session. Donc la session va prendre l'id d'un utilisateur et retourner l'objet utilisateur correspondant. 
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

def envoyer_courriel(jeton, email):
  msg = Message("Courriel d'activation", sender=app.config['MAIL_USERNAME'], recipients=[email])
  msg.body = f'''
  Pour activer votre compte cliquez sur ce lien :
  {url_for('activate_mail', jeton=jeton, _external=True)}
  '''
  mail.send(msg)

def generer_jeton_activation(mail):
  s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
  return s.dumps(mail, salt=app.config['SECURITY_PASSWORD_SALT'])

def confirmer_jeton(jeton, expiration=3600):
  s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
  try:
    mail = s.loads(jeton, salt=app.config['SECURITY_PASSWORD_SALT'], max_age=expiration)
  except:
    return False
  return mail




@app.route('/', methods=['POST', 'GET'])
def home():
  form = Inscription()
  if request.method == 'POST' and form.validate():
    hashed_password = bcrypt.generate_password_hash(form.mdp.data).decode('utf-8')
    user = User(nom=form.nom.data, email=form.mail.data, mdp=hashed_password)
    db.session.add(user)
    db.session.commit()
    
    # gestion de jeton et de confirmation
    jeton = generer_jeton_activation(user.email)
    envoyer_courriel(jeton, user.email)
    flash('Un courriel de validation vous a été envoyé' , 'success')
        
    return redirect(url_for('login'))
  else:
    return render_template('inscription.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
  form = Login()
  if request.method == 'POST' and form.validate():
    user = User.query.filter_by(email=form.mail.data).first()
    if user and bcrypt.check_password_hash(user.mdp, form.mdp.data):
      # f'/route/{variable}' remplace : '/route/{}'.format(variable)
      return redirect(f'/confirmation/{user.nom}')
    else:
      flash('Connexion impossible')
  else:
    return render_template('login.html', form=form)

@app.route('/confirmation/<string:nom>')
def confirmation(nom):
  return render_template('confirmation.html', nom=nom)

@app.route('/logout')
def logout():
  logout_user()
  flash('Vous etes deconnecté!', 'success')
  return redirect(url_for('home'))


@app.route('/activation/<string:jeton>')
def activate_mail(jeton):
  try:
    mail = confirmer_jeton(jeton)
  except:
    flash('Le lien est invalide ou a expiré', 'warning')
  user = User.query.filter_by(email=mail).first_or_404()
  if user.confirmation :
    flash('Le compte a déjà été confirmé, vous pouvez vous connecter', 'success')
    return redirect (url_for('login'))
  else:
    user.confirmation = True
    db.session.add(user)
    db.session.commit()
    flash("Vous avez confirmé votre compte", 'success')
  return redirect (url_for('login'))
    
  