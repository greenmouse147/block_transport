#!/usr/bin/env python3

from block import Block
from transaction import Transaction

if __name__ == '__main__':
    blockchain=[]
    transaction1=Transaction(clearMsg="This is a test", EncMsg="sqdknqsdoqsd", event=1, code=1)
    transaction2=Transaction(clearMsg="This is a test", EncMsg="sqdknqsdoqsd", event=1, code=1)
    geneseBlock = Block(None,
    					[transaction1,
    					 transaction2],
    					 'bb54068aea85faa7e487530083366be9962390af822e4c71ef1aca7033c83e66')
    blockchain.append(geneseBlock)

