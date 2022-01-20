# Solutions

1. What is ` __init__.py`

- Regular package vs namespace packages

https://docs.python.org/3/reference/import.html#regular-packages

2. What is `if __name__ == '__main__'`

https://stackoverflow.com/questions/419163/what-does-if-name-main-do

## Création d'un environnement virtuel :

1. Première possibilité :
````
$ python3.9 -m venv env
````

- `-m` permet le changement de module.
- `venv` le module qui permet la création d'un environnement virtuel.

Pour l'activation :

````
$ source env/bin/activate
````

Pour la désactivation :

`````
$ deactivate
`````

2. Deuxième possibilité :
````
$ pip3 install virtualenv
$ virtualenv -p python3.9 env
````

Pour l'activation et la désactivation utiliser les commandes précédentes.

## Conviguration du PATH du shell pyenv

1. Sur macOs :

````
$ ln -s -f /usr/local/bin/python3.9.7 /usr/local/bin/python
````

2. Sur Ubuntu :

````
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9.7 1

$ sudo update-alternatives --config python

$ sudo update-alternatives  --set python /usr/bin/python3.9.7
````
