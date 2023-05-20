import datetime 
import hashlib
import json
# from flask import Flask, jsonify, request

class BlockChain:

    def __init__(self):
        
        # Genesis Block 
        self.chain = []
        self.create_block(owner = "creater", Reg_no="005", proof = 1, previous_hash = "0")
    
    def create_block(self, owner, Reg_no, proof, previous_hash):
        block = {
            "owner": owner, 
            'Reg_no': Reg_no, 
            "index": len(self.chain) + 1,
            "proof": proof,
            "timestamp": str(datetime.datetime.now()),
            "previous_hash": previous_hash
        }
        self.chain.append(block)
        return block