from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from database import User

class Inscription(FlaskForm):
  nom = StringField("Nom de l'utilisateur", validators=[DataRequired()])
  mail = StringField("Adresse mail de l'utilisateur", validators=[DataRequired(), Email()])
  confirmation_mail = StringField("Confirmation de l'adresse mail", validators=[EqualTo('mail')])
  mdp = PasswordField("Mot de passe", validators=[DataRequired(), Length(min=8)])
  confirmation_mdp = PasswordField("Confirmation mot de passe", validators=[EqualTo('mdp')])
  
  submit = SubmitField("S'inscrire")
  
  def validate_email(self, mail):
    user = User.query.filter_by(email=mail.data)
    if user:
      raise ValidationError("Cette adresse mail existe déjà!")
    
class Login(FlaskForm):
  mail = StringField("Adresse mail", validators=[DataRequired(), Email()])
  mdp = PasswordField("Mot de passe", validators=[DataRequired()])
  remember = BooleanField("Se souvenir de moi")
  
  submit = SubmitField("Se connecter")