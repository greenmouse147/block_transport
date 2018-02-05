#!/usr/bin/env python3 

from Crypto.PublicKey import RSA

class Enterprise:

	def __init__(self):
		self.key = RSA.generate(4096)
		self.publicKey = self.key.publickey().exportKey()
		self.privKey = self.key.exportKey()


	def encryptData(self, data):
		return ""

	def decryptData(self, data):
		return ""


if __name__ == '__main__':
	a = User()
	print(a.publicKey)
	print(a.privKey)

