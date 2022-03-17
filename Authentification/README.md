# Solutions

## Qu'est-ce que SECRET_KEY (ou comment créer un cookie signé) ?

- Il s'agit d'une méthode permettant de garantir qu'un contenu n'a pas été modifié par quelqu'un d'autre qu'une personne ou une entité autorisée à le faire.

- Un cookie est généralement une donnée ajoutée par le serveur à une réponse HTTP par le biais de ses en-têtes. Il est conservé par le navigateur qui le renvoie ensuite au serveur lorsqu'il émet des demandes, également par le biais des en-têtes HTTP.<br/> 
La signature des cookies est une mesure préventive contre la falsification des cookies. Au cours du processus de signature d'un cookie, la clé `SECRET_KEY est utilisée d'une manière similaire à celle d'un "salt" utilisé pour brouiller un mot de passe avant de le hacher.


## Qu'est-ce que FlaskBcrypt ?

- Flask-Bcrypt est une extension Flask qui fournit des utilitaires de hachage bcrypt pour votre application.
- En raison de la récente augmentation de la prévalence de matériel puissant, comme les GPU modernes, les hachages sont devenus de plus en plus faciles à craquer. Une solution proactive à ce problème est d'utiliser un hachage qui a été conçu pour être "désoptimisé". Bcrypt est un tel dispositif de hachage ; contrairement aux algorithmes de hachage tels que MD5 et SHA1, qui sont optimisés pour la vitesse, bcrypt est intentionnellement structuré pour être lent.
- Pour les données sensibles qui doivent être protégées, comme les mots de passe, bcrypt est un choix conseillé.

- La fonction `generate_password_hash` nous permet de prendre 3 paramètres :
* Le mot de passe à hacher
* rounds : ce qui définit le paramétre `log_rounds` de la méthode `bcrypt.gensalt()` qui détérmine la complexité du salt. Par défaut la veleur est à 12.
* prefix : détérmine la version de l'algorithme utilisé pour créer le hachage. Prend la plus récente version par défaut.


 
