from shared import db
from dataclasses import dataclass

# décorateur permettant d'identifier un schema qui sera utilisé pas SQLAlchemy
@dataclass
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nom = db.Column(db.String(20), nullable=False)
  email = db.Column(db.String(120), nullable=False)
  mdp = db.Column(db.String(20), nullable=False)
  confirmation = db.Column(db.Boolean, nullable=False, default=False)