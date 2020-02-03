from flask_sqlalchemy import SQLAlchemy
from flask import Flask,Blueprint,render_template,redirect,request,flash,url_for,session,logging


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///generate.sqlite3"
db=SQLAlchemy(app)

class generate(db.Model):
    __tablename__="Users"
    s_No = db.Column(db.Integer,primary_key=True) 
    pin = db.Column(db.String(20),unique=True)
   
    def __init__(self, pin):
        self.pin = pin

db.create_all()

