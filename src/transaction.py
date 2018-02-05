#!/usr/bin/env python3
#codding : utf-8
import hashlib 
from time import strftime, gmtime 

class EventType(Exception):
	pass

class CodeType(Exception):
	pass


class Transaction:

	"""

		Transaction associated to the blockchain 

		cf : https://github.com/greenmouse147/block_transport 

	"""

	def __init__(self, publicKey, util, reputation, event, code,  privateKey, ):

		codeTypes = {
					1 : 'Alerte',
					2 : 'Ajout de réputation',
					3 : 'Retrait de réputation',
					4 : 'Création utilisation',
					5 : 'Création entreprise',
		}
		eventTypes = {
					1 : 'Accident',
					2 : 'Vol',
					3 : 'Agression',
					4 : 'Incendie',
					5 : 'Retard',
		}
		if code < 1 or code > 5:
			raise EventType("Out of range event type (1-5), you specified {:d}".format(code))
		if event < 1 or event > 5:
			raise CodeType("Out of range code type (1-5), you specified {:d}".format(event))

		

		#Detection type de trame
		self.transactionType = codeTypes[event]
		if self.transactionType == 4
			new_user = user()
			
			self.util == None
			self.reputation = 5
			self.event = None
			
		else :
			self.util = util
			self.reputation = reputation
			self.code = code 
		


		self.publicKey = publicKey		
		self.privateKey = privateKey
		
		self.codeType = eventTypes[code]
		self.time = strftime("%d %b %Y %H:%M:%S +0000", gmtime())
		self.hashClearMsg = hashlib.sha256(clearMsg.encode('utf-8')).hexdigest()
		self.hashEncMsg = hashlib.sha256(EncMsg.encode('utf-8')).hexdigest()
		self.gps = None 

if __name__ == '__main__':

	a = Transaction(clearMsg="This is a test", EncMsg="sqdknqsdoqsd", event=1, code=1)
	print(a.time)
