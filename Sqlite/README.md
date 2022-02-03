# Solutions

L'enoncé du laboratoire est disponible [ici](./enonce.md)

## Fonctionnement

_Préalables_ : activation de l'environnement virtuel.

- On commence par créer la base de données `musique.db`

````
$ cd db
$ sqlite3 musique.db
````

- Une fois la console sqlite3 ouverte :

````
> .read script.sql
````

- Autre méthode :

````
$ sqlite3 musique.db < script.sql
````

- On peut en suite lancer le script python :

`````
$ cd ..
$ python main.py
`````

## Plus loin :

- https://www.sqlalchemy.org/
- https://flask-sqlalchemy.palletsprojects.com/en/2.x/
