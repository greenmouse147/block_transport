#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from database import transportDB


class User:

	def __init__(self):
		self.key = RSA.generate(4096)
		self.publicKey = self.key.publickey().exportKey()
		self.privKey = self.key.exportKey()
		self.reputation = 5


	def encryptData(self, data):
		return

	def createUser(self):
		db = transportDB()
		db.execQuery("wallet.db",'INSERT INTO wallets (privateKey, publicKey, reputation) VALUES ("9b4def4337de386a795e0c1ea0f90d7583261db2", "9b4def4337de386a795e0c1ea0f90d7583261db2", 5')

#



if __name__ == '__main__':
	a = User()
	a.createUser()
	print(a.publicKey)
	print(a.privKey)
