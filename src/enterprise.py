#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from database import transportDB

WALLET_DB_FILE = "wallet.db"
WALLET_TEMPLATE_FILE = "wallet.sql"

class Enterprise:

	def __init__(self):
		self.key = RSA.generate(4096)
		self.publicKey = self.key.publickey().exportKey()
		self.privKey = self.key.exportKey()
		self.reputation = 0
		self.db = transportDB()

	def encryptData(self, data):
		return ""

	def decryptData(self, data):
		return ""

	def createEnterprise(self):
		if not isfile(WALLET_DB_FILE):
			self.db.createDB(WALLET_TEMPLATE_FILE,WALLET_DB_FILE)
		self.db.execQuery(WALLET_DB_FILE,'INSERT INTO wallets (privateKey, publicKey, reputation) VALUES (?, ?, ?)',(str(self.privKey), str(self.privKey), self.reputation))


if __name__ == '__main__':
	a = User()
	print(a.publicKey)
	print(a.privKey)
