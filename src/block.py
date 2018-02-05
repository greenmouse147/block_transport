#!/usr/bin/env python3 

class Block:
	def __init__(self, previousHash, transactions, hash):

		""" 
			Basic block structure, : 

				previousBlock ==> Address of precedent block 

				transactions ==> [block_transport1, block_transport2, ..]

				hash ==> sha256 of transactions pool ? 
		"""

		self.previousHash=previousHash
		self.transactions=transactions
		self.hash=hash


