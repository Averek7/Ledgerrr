import os
from ledger import *
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, world!"


@app.route('/isValid', methods=['GET'])
def isValid():
    isValid = BlockChain.isChainValid(BlockChain.chain)
    if isValid:
        response = {'message', 'Legder valid'}
    else: 
        response = {'message','Record violation'}
    
    return jsonify(response), 200

@app.route('/mineBlock', methods=['POST'])
def mineBlock():
    val = request.get_json()
    required = ['owner', 'Reg_no']
    if not all (k in val for k in required):
        return 'Missing Values', 404
    
    owner = val['owner']
    Reg_no = val['Reg_no']
    previous_block = BlockChain.getPreviousBlock()
    previous_proof = previous_proof['proof']
    proof = BlockChain.proof_work(previous_block)
    previous_hash= BlockChain.hash(previous_block)

    block = BlockChain.create_block(owner, Reg_no, proof, previous_hash)

    response = {'mesage', 'Record Merged to Ledger'}

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)

