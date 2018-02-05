#!/usr/bin/env python3

from block import Block

if __name__ == '__main__':
    blockchain=[]
    geneseBlock = Block(None,
    					['Train Maubeuge/Paris en retard',
    					 'Agression à la friterie de Maubeuge'],
    					 'bb54068aea85faa7e487530083366be9962390af822e4c71ef1aca7033c83e66')
    blockchain.append(geneseBlock)

