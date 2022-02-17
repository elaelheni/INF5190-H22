#
# Ce script contient un exemple d'utilisation de flask-sqlalchemy
#
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#desactiver les messages qui apparaissent a la console avec chaque modification de la base de données
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#permet d'établir une connexion avec ma base de données
# /// pour ajouter le chemin relatif vers la base de données
# //// pour ajouter le chemin absolu
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'

db = SQLAlchemy(app)

#Creer la table Person et les colomnes demandées
class Person(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  sex =db.Column(db.Integer, default=0)
  age = db.Column(db.Integer, nullable=False)
  town = db.Column(db.String(50), nullable=False)
  
  # p = Person(name="Steeve", sex=9, age=57, town="Paris")
  # db.create_all()
  
@app.route('/')
def home():
  persons = Person.query.all()
  return render_template("home.html", persons=persons)

@app.route("/get-info/<int:id>")
def get_info(id):
  p = Person.query.get_or_404(id)
  return render_template("infos.html", p=p)

#
# Exemple : chercher une personne avec son nom, si la presonne existe retourner toutes ses infos
# sinon un 404.
#
@app.route("/<string:name>")
def get_person(name):
  p = Person.query.filter_by(name=name).first_or_404()
  return f"Les informations : {p.name}, {p.age}, {p.sex}"