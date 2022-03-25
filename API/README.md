# Solutions

L'enonce du labo se trouve [ici](./enonce.md).

## API REST
API REST (Representational State Transfer Application Program Interface) est un style architectural qui permet aux logiciels de communiquer entre eux sur un réseau ou sur un même appareil. Le plus souvent les développeurs utilisent des API REST pour créer des services web. Souvent appelés services web RESTful, REST utilise des méthodes HTTP pour récupérer et publier des données entre un périphérique client et un serveur.

En utilisant le protocole HTTP, les API REST permettent aux logiciels d’un appareil de communiquer avec les logiciels d’un autre appareil (ou du même appareil) même s’ils utilisent des systèmes d’exploitation et des architectures différents. Le client peut demander des ressources avec un langage que le serveur comprend, et le serveur renvoie la ressource avec un langage que le client accepte. Le serveur renvoie la ressource au format JSON (JavaScript Object Notation), XML (Extensible Markup Language) ou texte, mais de nombreuses API prennent en charge d’autres langages.


## Introduction

Dans le monde des API, la validation consiste à vérifier si les données envoyées sont bonnes ou non. Vous ne pouvez jamais vous fier entièrement à une validation côté client.<br>
Comme vous ne savez pas ce qui se passe sur le client, vous ne pouvez pas faire confiance aux données que vous recevez.<br>
Même si vous avez une API privée, quelqu'un peut toujours vous envoyer des requêtes non valides.<br>
La validation côté serveur implique de vérifier plusieurs choses, entre autre :
- quelles sont les propriétés attendues
- ont-elles le bon format/type
- la propriété est-elle requise ?


## JSON Schema
Le schéma JSON est un moyen de décrire toute instance de données JSON, comme celles que l'on trouve dans notre requête ou réponse HTTP.<br>
Le mot-clé type limitera votre propriété à un certain type. Il existe plusieurs valeurs possibles :<br>
- string
- number
- object
- array
- boolean
- null

1. Exemple :
Vous pouvez vous assurer que votre paramètre se trouve à l'intérieur d'une certaine plage avec des paramètres supplémentaires :
- x ≥ minimum
- x > exclusiveMinimum
- x ≤ maximum
- x < exclusiveMaximum

````
"my_param": { 
    "type": "number",
    "minimum": 0,
    "maximum": 100
}
````
Il est possible de faire cette double validation avec la majorité des types cités plus haut.<br>
Exemple pour `string` :
````
"firstname": {
    "type": "string",
    "minLength": 2,
    "maxLength": 50
}
````

## Validation avec Flask

Il y a plusieurs paquets python qui font de la validation basée sur JSON Schema. Personnellement, j'utilise `flask_json_schema` :

````
$ pip install flask_json_schema
````

Le paquet fonctionne simplement comme un décorateur pour les endpoints Flask :

````
insert_schema = {
    'type' : 'object',
    'required' : ['titre', 'auteur', 'annee', 'nb_pages', 'nb_chapitres'],
    'properties' : {
        'titre' : {
            'type' : 'string'
        },
        'auteur' : {
            'type' : 'string'
        },
        'annee' : {
            'type' : 'number'
        },
        'nb_pages' : {
            'type' : 'number'
        },
        'nb_chapitres' : {
            'type' : 'number'
        }
    },
    'additionalProperties' : False
}

@app.route('/api/livre', methods=['POST'])
@schema.validate(insert_schema)
def create_livre():
...

````

Si la requête reçue ne correspond pas au schéma, une erreur sera levée. Et le code 400 sera envoyé comme réponse.

### Plus loin : Ignorer les validations des méthodes

Si votre endpoint a plusieurs méthodes, vous pouvez ignorer la validation pour certaines d'entre elles.

````
@app.route('/api/livre', methods=['POST'])
@expects_json(schema, ignore_for=['GET'])
def create_livre():
...
````

