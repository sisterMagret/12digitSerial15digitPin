from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///generate.sqlite3"
db=SQLAlchemy(app)

class generate(db.Model):
    __tablename__="Users"
    id = db.Column(db.Integer, unique=True, primary_key=True)
    pin = db.Column(db.String(16),unique=True)
   
    def __init__(self, pin):
        self.pin = pin

db.create_all()

