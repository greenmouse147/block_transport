import sqlite3
from os.path import isfile

class transportDB(object):
    """ database class """

    def execQuery(self, inputDBFile, query, args = False):
        if isfile(inputDBFile):
            self.connexion = sqlite3.connect(inputDBFile)
            self.cursor = self.connexion.cursor()

            #check https://docs.python.org/2/library/sqlite3.html
            if args:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query)
                self.connexion.commit()
                self.connexion.close()
        return res


    def createDB(self, inputDBTemplate , outputDBFile):
        outputDBFile = str(outputDBFile) + ".db"
        # maak db met genesis transaction en wallet
        with open(inputDBTemplate,"r") as f:
            sql = f.read()
            tmpConn = sqlite3.connect(outputDBFile)
            tmpCursor = tmpConn.cursor()
            tmpCursor.executescript(sql)
            tmpConn.commit()
            tmpConn.close()
        f.close()
