#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from database import transportDB
from os.path import isfile


WALLET_DB_FILE = "wallet.db"
WALLET_TEMPLATE_FILE = "wallet.sql"

class User:

	def __init__(self):
		self.key = RSA.generate(4096)
		self.publicKey = self.key.publickey().exportKey()
		self.privKey = self.key.exportKey()
		self.reputation = 5
		self.db = transportDB()



	def encryptData(self, data):
		return

	def createUser(self):
		if not isfile(WALLET_DB_FILE):
			self.db.createDB(WALLET_TEMPLATE_FILE,WALLET_DB_FILE)
		self.db.execQuery(WALLET_DB_FILE,'INSERT INTO wallets (privateKey, publicKey, reputation) VALUES (?, ?, ?)',(str(self.privKey), str(self.privKey), self.reputation))



if __name__ == '__main__':
	a = User()
	a.createUser()
	print(a.publicKey)
	print(a.privKey)
