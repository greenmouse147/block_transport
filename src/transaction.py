#!/usr/bin/env python3

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

	def __init__(self, publicKey, clearMsg, EncMsg, event, code):

		eventTypes = {
					1 : 'Alerte',
					2 : 'Ajout de réponses',
					3 : 'Retrait de réputation',
					4 : 'Création utilisation',
					5 : 'Création entreprise',
		}
		codeTypes = {
					1 : 'Accident',
					2 : 'Vol',
					3 : 'Agression',
					4 : 'Incendie',
					5 : 'Retard',
		}
		if event < 1 or event > 5:
			raise EventType("Out of range event type (1-5), you specified {:d}".format(event))
		if code < 1 or code > 5:
			raise CodeType("Out of range code type (1-5), you specified {:d}".format(code))
		self.publicKey = publicKey
		self.transactionType = eventTypes[event]
		self.codeType = codeTypes[code]
		self.time = strftime("%d %b %Y %H:%M:%S +0000", gmtime())
		self.hashClearMsg = hashlib.sha256(clearMsg.encode('utf-8')).hexdigest()
		self.hashEncMsg = hashlib.sha256(EncMsg.encode('utf-8')).hexdigest()
		self.gps = None 

if __name__ == '__main__':

	a = Transaction(clearMsg="This is a test", EncMsg="sqdknqsdoqsd", event=1, code=1)
	print(a.time)

