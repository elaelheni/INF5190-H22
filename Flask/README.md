# Remarques & astuces

1. Framework :
 Un framework est un outil permettant de grandement faciliter le developpement dans un domaine d'application particulier. Il va permettre de rendre le travail facile à l'interieur de son périmètre (exple : developper des application web avec Django) mais extrement difficile à l'extérieur de son périmètre (exple : developper des application Microsoft avec Django).

2. Framework web :
 Les frameworks Web offrent un moyen standard de créer et de déployer des applications Web sur le World Wide Web.

3. Microframework :
"Micro" ne signifie pas que toute votre application web doit tenir dans un seul fichier Python (bien que ce soit certainement possible), ni que Flask manque de fonctionnalités. Le "micro" de microframework signifie que Flask vise à garder le noyau simple mais extensible. Flask ne prendra pas beaucoup de décisions pour vous, comme le choix de la base de données à utiliser. Les décisions qu'il prend, comme le moteur de templating à utiliser, sont faciles à modifier. Tout le reste dépend de vous, de sorte que Flask puisse être tout ce dont vous avez besoin et rien que vous n'ayez besoin.
Par défaut, Flask n'inclut pas de couche d'abstraction de base de données, de validation de formulaire ou quoi que ce soit d'autre là où il existe déjà des bibliothèques différentes qui peuvent gérer cela. Au lieu de cela, Flask supporte des extensions pour ajouter de telles fonctionnalités à votre application comme si elles étaient implémentées dans Flask lui-même. De nombreuses extensions permettent l'intégration de bases de données, la validation de formulaires, la gestion des téléchargements, diverses technologies d'authentification ouverte, etc. Flask est peut-être "micro", mais il est prêt à être utilisé en production pour une variété de besoins.

*Source : https://flask.palletsprojects.com/en/2.0.x/foreword/#what-does-micro-mean*

4. Autres explications pértinentes:

L'URL est l'identifiant unique d'une *ressource* sur le web. La route est un chemin vers cette ressource.

L'URL contient :
- Le protocole de communication utilisé (http, https.. dans notre cas)
- Le nom du domaine ou l'adresse IP (exemple : uqam.ca)
- Le port (pour le protocole http, le port est part défaut 80, sinon il est précisé après le nom du domaine)
- Une route (qui est un chemain vers une ressource)
- Des paramètres

Http est le protocole qui permet l'échange de pages web.

Jinja est un moteur de templation. Plutot que de générer des chaines de caractères directement dans le backend nous allons utiliser des templates.
Les templates sont simplement des fichiers HTML avec probablement des annotations en Jinja.

Ces fichiers vont par défaut se trouver dans le répértoire `templates` qui doit etre au meme niveau que le script python contenant les routes de l'application.

De façon plus vulgaire, Jinja va permettre un echange d'informations du backend (les scripts python) vers le frontend (le fichier HTML).


# Pour lancer l'application :

1. On commence par installer `flask` :

```
  $ pip install flask
```

2. On import les variables d'environnement nécessaires :

```
$ export FLASK_APP=app.py
$ export FLASK_DEBUG=1

```
3. On lance l'application :

```
$ flask run
```
