#!/usr/bin/env python3

from Crypto.PublicKey import RSA

wallet_prefix = "user"

class User:

	def __init__(self):
		self.key = RSA.generate(4096)
		self.publicKey = self.key.publickey().exportKey()
		self.privKey = self.key.exportKey()
		self.reputation = 5


	def encryptData(self, data):
		return




if __name__ == '__main__':
	a = User()
	print(a.publicKey)
	print(a.privKey)
