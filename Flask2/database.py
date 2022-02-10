import sqlite3

class Database:
  def __init__(self):
    self.connection = None
    
  def get_connection(self):
    if self.connection is None:
      self.connection = sqlite3.connect('db/personne.db')
    return self.connection
  
  def disconnect(self):
    if self.connection is not None:
      self.connection.close()
      
  def get_all_persons(self):
    cursor = self.get_connection().cursor()
    cursor.execute("SELECT nom, prenom, age FROM personne ORDER BY nom")
    persons = cursor.fetchall()
    return persons
  
  def add_person(self, nom, prenom, age):
    connection = self.get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO personne(nom, prenom, age)" "VALUES(?,?,?)", (nom, prenom, age))
    connection.commit()