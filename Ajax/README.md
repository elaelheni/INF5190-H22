# Solutions

## Remarques :
1. Synchrone vs asynchrone :

- Les échanges entre le frontend et le backend sont généralement synchrones, on va donc attendre de recevoir la réponse du serveur avant de continuer l'execution du JavaScript.
- Il est possible d'avoir des échanges asynchrones dans le but d'améliorer la convivialité au niveau du frontend ou d'éviter le full page refresh, dans ce cas on continue l'execution du Javascript et une fonction sera appelée lorsque la réponse du serveur devient disponible.

2. SQLAlchemy :

- Il s'agit d'un mappeur object-relationnel qui offre toute la puissance et la flexibilité de SQL.
- Il est conçu pour un accès efficace et performant aux bases de données, adapté dans un langage de domaine simple en python (plus besoin d'utiliser des requetes SQL).

Quelques organisations qui l'utilisent : Yelp!, reddit, Dropbox..

## Version 2:

1. Ouvrir la console Python
2.
```
> from app import db, Person
> db.create_all()
> p = Person(name="Charlotte", sex=2, age=23, town="Montreal")
> db.session.add(p)
> db.session.commit()
> exit()

```

### Manipulations console SQLite3:
1. Pour vérifier que la table a été créé :
```
sqlite3 database.db
> .tables
> .exit
```
2. Pour afficher le contenu de la table : 
```
sqlite3 database.db
> select * from person;
> .exit
```
