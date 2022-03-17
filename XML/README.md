# Solutions

## Exercice 1

Après correction : 
```
<?xml version="1.0" encoding="utf-8" standalone="yes"?>

<library>
  <documents>
    <document type="book">
      <title>Théorie de la musique</title>
      <author>A. Danhauser</author>
      <year>1996</year>
    </document>
    <document type="book">
      <title>Test-Driven Development by Example</title>
      <author>Kent Beck</author>
      <year>2003</year>
    </document>
    <document type="book">
      <title>Design Patterns - Elements of Reusable Object-Oriented Software</title>
      <author>Erich Gamma</author>
      <author>Richard Helm</author>
      <author>Ralph Johnson</author>
      <author>John Vlissides</author>
      <year>1995</year>
    </document>
    <document type="article">
      <title>XML Schema</title>
      <author>Eric van der Vlist</author>
      <year>2001</year>
  </document>
</documents>
</library>

```

## Exercice 2

Version atelier :

Cliquez [ici](./exercice2.xml)

Version Jacques :

```
<?xml version="1.0" encoding="utf-8"?>
<dossier>
  <nom>Berger</nom>
  <prenom>Jacques</prenom>
  <NAM>BERJ99999901</NAM>
  <medecin>
    <nom>Stevenson</nom>
    <prenom>Steven</prenom>
    <identifiant>99330-10</identifiant>
    <ville>Sorel-Tracy</ville>
  </medecin>
  <visites>
    <visite>
      <date>2010-01-12</date>
      <sujet>Perte de cheveux</sujet>
      <description>Le patient ne perd pas ses cheveux, il a plutôt des allucinations. Des calmants ont été prescrits.</description>
    </visite>
    <visite>
      <date>2010-01-28</date>
      <sujet>Blessure au genou</sujet>
      <description>Les calmants provoquent des allucinations plus fortes et le patient a fait une mauvaise chute. Des anti-inflammatoires ont été prescrits. La prise de calmants est suspendu.</description>
    </visite>
    <visite>
      <date>2010-02-14</date>
      <sujet>Dépression</sujet>
      <description>Le patient est déprimé car il est seul à la St-Valentin. Aucune prescription, un simple câlin a réglé la situation.</description>
    </visite>
  </visites>
</dossier>

```
