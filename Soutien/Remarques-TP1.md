# Quelques remarques à considérer pour le TP1


1. Les 5 derniers articles en date du jour :

```
date_today = date.today()
cursor.execute("select * from article where dtae_publication  <= ? limit 5" , (date_today,))
```

2. Fonctionnalité de recherche en utilisant l'operateur LIKE 

```
cursor.execute(("select titre, date_publication, identifiant from article where titre like ? or paragraphe like ?"), ('%'+texte+'%', '%'+texte+'%'))
```

3. Validations de la date 

- Format ISO8601 (AAAA-MM-DD)
- Faire attention aux dates innexistantes (ex : 2022-02-31)
- Faire attention aux années bisextiles (ex: 2023-02-29)
- On peut prévoir la publication d'un article dans le futur, pas au passé

4. Validation HTML5 & CSS3 : https://validator.w3.org/

## Attention :
Si vous utilisez du code source qui n'est pas le votre (Stackoverflow, exemples du cours, labos...) n'oubliez pas de citer les sources dans votre README.
