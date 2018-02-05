import sqlite3

#TRANSPORT_BLOCKCHAIN_DB_FILE = "transport.db"
#TRANSPORT_DB_TEMPLATE = "transport.sql"

class transportDB():
  """ Classe permettant la gestion de la base de donnée """
  def __init__(self, bddFile, bddTemplate):
      self.bddFile = bddFile
      self.bddTemplate = bddTemplate

  def execQuery(self, query, args = False, result = "all")
    self.connexion = sqlite3.connect(self.dbFile)
    #like sql3 documentation https://docs.python.org/2/library/sqlite3.html
    self.cursor = self.connexion.cursor()

    if args :
        self.cursor.execute(query, args)
    else:
        self.cursor.execute(query)

    res = ""
    if result == "all":
        res = transport.db.cursor.fetchall()
    if result == "one":
        res = transport.db.cursor.fetchone()

    self.connexion.commit()
    self.connexion.close()

    return res

    def initDB():
        """ Classe permettant d'initiliser la base de donnée à partir du
         fichier template
         Permet aussi de créer un wallet
         """
         sql = open(self.bddTemplate, 'r').read()
         tmpConnexion = sqlite3.connect(self.dbFile)
         tmpCursor = tmpConnexion.cursor()
         tmpCursor.executescript(sql)
         tmpConnexion.commit()
         tmpConnexion.close()
