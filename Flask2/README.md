# Solutions

L'enonce est disponible [ici](./enonce.md)

## Remarques :

- Le contexte d'application conserve la trace des données de niveau application pendant une requête, une commande CLI ou toute autre activité. Plutôt que de transmettre l'application à chaque fonction, on accède aux proxies `current_app` et` g` à la place.
- Le contexte de l'application est un bon endroit pour stocker les données communes pendant une requête ou une commande CLI. Flask fournit l'objet `g` dans ce but. Il s'agit d'un simple objet d'espace de nom qui a la même durée de vie qu'un contexte d'application.
