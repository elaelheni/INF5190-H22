import sqlite3

class Database:
  def __init__(self):
    self.connection = None
    
  def get_connection(self):
    if self.connection is None:
      self.connection = sqlite3.connect('db/database.db')
    return self.connection
  
  def disconnect(self):
    if self.connection is not None:
      self.connection.close()
      
  def insert_user(self, nom, courriel, date_inscription, mdp):
    connection = self.get_connection()
    connection.execute("INSERT INTO compte (nom, courriel, date_inscription, mdp)" "VALUES (?,?,?,?)", (nom, courriel, date_inscription, mdp))
    connection.commit()
    
    
  def mail_exists(self, courriel):
    cursor = self.get_connection().cursor()
    cursor.execute("SELECT * FROM compte WHERE courriel LIKE?", ('%'+courriel+'%',))
    exists = cursor.fetchall()
    if len(exists) == 0:
      return False
    else:
      return True
  