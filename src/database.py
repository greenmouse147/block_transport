import sqlite3

DB_FILE = 'wallet.db'


class TransportBlockBD(object):
    """ database class """
    def __init__(self, dbFile = DB_FILE):
        self.dbFile = dbFile

    def execQuery(self, query, args = False):

        self.connexion = sqlite3.connect(self.dbFile)
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
        sql = open(inputDBTemplate,'r').read()
        tmpConn = sqlite3.connect(outputDBFile)
        tmpCursor = tmpConn.cursor()
        tmpCursor.executescript(sql)
        tmpConn.commit()
        tmpConn.close()

if __name__ == '__main__':
     c = TransportBlockBD()
     c.createDB("block.sql","block")
