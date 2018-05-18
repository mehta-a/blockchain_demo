import sys

sys.path.append('c:\\programdata\\anaconda3\\lib\\site-packages')

# Part II - Mining our Blockchain
from flask import Flask, jsonify
from blockchain import Blockchain

# Creating a Web App
app = Flask(__name__)

# Creating a Blockchain
blockchain = Blockchain()

# Default
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Mining a new block
@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congratulations! you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200

# Getting the full blockchain
@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

# Check if blockchain is valid or not
@app.route('/is_valid', methods = ['GET'])
def get_chain():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'All Good. The blockchain is valid.'}
    else:
        response = {'message': 'Houston, we have a problem. The blockchain is valid.'}
    return jsonify(response), 200
# Running the app
app.run(port = 5000)

print("Finished building Part II - mining a blockchain...")