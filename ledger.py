import datetime 
import hashlib
import json

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
    
    def proof_work(self, previous_proof):
        new_proof = 1
        checkProof = False

        while checkProof is False:
            hashVal = hashlib.sha256(str(new_proof**2-previous_proof**2).encode()).hexdigest()

            if hashVal[:4] == '0000':
                checkProof = True
            else:
                new_proof += 1
        
        return new_proof
    
    def hash(self, block):
        encodeBlock = json.dumps(block).encode()     # converts block(dict) to string
        return hashlib.sha256(encodeBlock).hexdigest()
    

    def isChainValid(self, chain):
        previousBlock = chain[0]
        blockIdx = 1

        while blockIdx < len(chain):
            block = chain[blockIdx]
            if block['previous_hash'] != self.hash(previousBlock):
                return False
            
            previousProof = previousBlock['proof']
            proof = block['proof']
            hashVal = hashlib.sha256(str(proof**2-previousProof**2).encode()).hexdigest()

            if hashVal[:4] != '0000':
                return True
            
            previousBlock = block
            blockIdx += 1

        return True

    def getPreviousBlock(self):
        return self.chain[-1]
