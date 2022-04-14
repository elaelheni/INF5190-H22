from flask import Flask, render_template, session, redirect, url_for, request, flash
from authlib.integrations.flask_client import OAuth
from datetime import timedelta
import os
from auth_decorator import login_required
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.secret_key=os.getenv("APP_SECRET_KEY")
app.session_cookie_name=os.getenv("SESSION_COOKIE_NAME")
app.config.permanent_session_lifetime=os.getenv("PERMANENT_SESSION_LIFETIME")

oauth = OAuth(app)
google = oauth.register(
  name='google',
  client_id=os.getenv("GOOGLE_CLIENT_ID"),
  client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
  access_token_url="https://accounts.google.com/o/oauth2/token",
  access_token_params=None,
  authorize_url='https://accounts.google.com/o/oauth2/auth',
  authorize_params=None,
  api_base_url='https://www.googleapis.com/oauth2/v1/',
  userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
  client_kwargs={'scope': 'openid email profile'},
)

@app.route('/')
@login_required
def home():
  return render_template('index.html')

@app.route('/login')
def login():
  google = oauth.create_client('google')
  redirect_url = url_for('authorize', _external=True)
  return google.authorize_redirect(redirect_url)

@app.route('/authorize')
def authorize():
  google = oauth.create_client('google')
  token = google.authorize_access_token()
  resp = google.get('userinfo')
  user_info = resp.json()
  session['profile'] = user_info
  session['page'] = 1
  session.permanent = False
  return redirect('/')


@app.route('/page1', methods=['GET', 'POST'])
@login_required
def page1():
  if session['page'] != 1 :
    return "Non authorisé!", 401
  else:
    if request.method == 'GET':
      return render_template("page1.html")
    else:
      nom = request.form["nom"]
      prenom = request.form["prenom"]
      ville = request.form["ville"]
      # TODO gerer les erreurs
      session['nom'] = nom
      session['prenom'] = prenom
      session['ville'] = ville
      session['page'] = 2
      return redirect('/page2')
    
@app.route('/page2', methods=["GET", "POST"])
@login_required
def page2():
  if session['page'] != 2 :
    return "Non authorisé!", 401
  else:
    if request.method == "GET":
      email = dict(session)['profile']['email']
      return render_template("page2.html", email=email)
    else:
      if request.form.get('valide'):
        session['page'] = 3
        return redirect('/page3')
      else:
        flash('Y a une erreur!')
        return redirect('/page2')

@app.route('/page3', methods=["GET", "POST"])
@login_required
def page3():
  if session['page'] != 3 :
    return "Non authorisé!", 401
  else:
    if request.method == "GET":
      return render_template("page3.html")
    else:
      enfant = request.form.get('liste-enfant')
      session['enfant'] = enfant
      # TODO enregistrement dans la bd
      # en utilisant tout ce qui a été stocké dans la session
      return redirect('/confirmation')

@app.route('/confirmation')
@login_required
def confirmation():
  name = session['prenom']
  return render_template("confirmation.html", name=name)

@app.route('/logout')
def logout():
  for key in list(session.keys()):
    session.pop(key)
  return redirect('/')

