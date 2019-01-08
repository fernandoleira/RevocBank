from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import sha256
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    balance = db.Column(db.Float)
    pwdhash = db.Column(db.String(54))

    def __init__(self, firstname, lastname, username, email, password):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.username = username.title()
        self.email = email.lower()
        self.balance = 0.0
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)


class Block:
    def __init__(self, transactions, previous_hash):
        self.time_stamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_header = str(self.time_stamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()

    def print_contents(self):
        conts = list()
        conts.append("timestamp: {}".format(self.time_stamp))
        conts.append("transactions: {}".format(self.transactions))
        conts.append("current hash: {}".format(self.generate_hash()))
        conts.append("previous hash: {}".format(self.previous_hash))

        return conts


class Blockchain:
    def __init__(self):
        self.chain = []
        self.unconfirmed_transactions = []
        self.genesis_block()

    def genesis_block(self):
        transactions = []
        genesis_block = Block(transactions, "0")
        genesis_block.generate_hash()
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        previous_hash = (self.chain[len(self.chain) - 1]).hash
        new_block = Block(transactions, previous_hash)
        new_block.generate_hash()
        # proof = proof_of_work(block)
        self.chain.append(new_block)

    def print_blocks(self):
        res = []
        for i in range(len(self.chain)):
            b = []
            current_block = self.chain[i]
            b.append("Block {} {}".format(i, current_block))
            b += current_block.print_contents()

            res.append(b)

        return res

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.generate_hash():
                print("Current hash does not equal generated hash")
                return False
            if current.previous_hash != previous.generate_hash():
                print("Previous block's hash got changed")
                return False
        return True

    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()
        while proof[:2] != "0" * difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof
