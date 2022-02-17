# Révision à l'examen intra

Q1 : Considérant la methode 'POST', comment obtenir la valeur d'un champ à partir d'un input de type text ?
-> request.form["`name`"]

Q2 : Considérent la méthode 'GET', comment obtenir la valeur d'un champ à partir d'un input de type text ? (Indice : utilisation des query parameters)
-> request.args.get("`name`")

Q3 : Est-ce que le moteur de templating Jinja2 est interprété par le fureteur ?
-> Nom

Q4 : Quel port est écouté par défaut par un serveur HTTP ?
-> 80

Q5 : Quel port est écouté par défaut par une application Flask ?
-> 5000

Q6 : Quel format de données le serveur peut utiliser pour envoyer des données au client ?
-> HTML, JSON, PDF, CSV, XML, ...

Q7 : Est-ce plus sécuritaire quand le frontend utilise directement une base de données ?
-> Non

Q8 : Est-ce vrai qu'aucun utilisateur ne peut lire le code du frontend ?
-> Non

Q9 : Quelles méthodes HTTP sont elles supportées par les formulaires HTML ?
-> GET et POST

Q10 : Existe-t-il une méthode HTTP permettant d'envoyer un mot de passe chiffré automatiquement dans un formulaire HTML ?
-> Non

Q11 : Quel est le code de statut HTTP retourné lorsqu'une requete de type GET a réussi ?
-> 200

Q12 : Quel est le code de statut HTTP retourné lors d'une demande de redirection ?
-> 201

Q13 : Quel est le code de statut HTTP retourné lorsqu'une requete de type POST ne contient pas toutes les données demandées ?
-> 400

Q14 : Quel est le code de statut HTTP retourné lors d'une erreur au niveau du serveur ?
-> 500

Q15 : Quel est le type de données utilisé pour stocker une image binaire dans une base de données SQlite ?
-> blob

Q16 : Comment générer une page 404 avec Flask ?
-> return render_templae("404.html"), 404

Q17 : Quel outil permet de vérifier que le code source d'un projet respecte les conventions de style Python ?
-> pycodestyle

Q18 : Comment assurer une facilité dans un changement futur dans le type d'une base de données ?
-> Isoler le code qui utilise la base de données

Q19 : Est-ce vrai que des gabarits Jinja2 peuvent se retrouver dans le répertoire static de Flask ?
-> Non

Q20 : Que représente la ligne de code suivante : `@app.route("/home")` ?
-> Un décorateur définissant une route
