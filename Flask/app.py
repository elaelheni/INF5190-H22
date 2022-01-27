from flask import Flask, render_template, request, redirect
from datetime import date

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    # print(error)
    return render_template("404.html"), 404


"""
Premier essai : envoyer un un simple Hello World dans le fureteur
@app.route("/", methods=["GET", "POST"])
def hello_world():
    return "<p>Hello World!</p>"
"""

"""
Deuxième essai : envoyer du contenu du backend vers le frontend via une variable jinja
@app.route("/", methods=["GET", "POST"])
def hello_world():
    today = date.today()
    return render_template("home.html", today=today)
"""

"""
Plusierus routes qui pointes vers la meme opération
"""


@app.route("/index", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home():
   # Si le client envoie une requete GET, on affiche le formulaire
    if request.method == "GET":
        return render_template("home.html")
    # Sinon la méthode est POST, on récupère les informations entrées
    else:
        text = request.form["text"]
        radio = request.form.get("radio") != None
        select = request.form.get("liste-choix")
        # verification simple des champs non vide
        if text == "" or radio == "" or select == "":
            # envoyer une variable interprétable par Jinja2
            return render_template("home.html", error="Tous les champs sont obligatoires!")
            # Plusieurs autres validations peuvent etre faites de la meme façon
        else:
            # Si valides, on écrit les informations récupérées dans le fichier log.txt
            log = open("log.txt", "w")
            log.write("text :%s" % text + "\nradio : %s" %
                      radio + "\nselect : %s" % select)
            log.close()
            # Par mesure de sécurité toujours fermer le fichier après traitement
            return redirect("/confirmation")


@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")
