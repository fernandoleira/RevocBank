from flask import Flask
from models import db, User, Blockchain

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://segsparp:4iIe8RBmaR0fpFAKeoYVcp0ovJxkzVzo@baasu.db.elephantsql.com:5432/segsparp'
db.init_app(app)

app.secret_key = 'development-key'

revoc_blockchain = Blockchain()

# App key
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.db_key = "This is a key123"

from routes import *

if __name__=="__main__":
    app.run(debug=True)