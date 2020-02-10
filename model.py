from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///generate.sqlite3"
db=SQLAlchemy(app)

class generate(db.Model):
    __tablename__="Users"
    id = db.Column(db.Integer, unique=True, primary_key=True)
    #s_No = db.Column(db.String(13),unique=True,nullable=False)
    pin = db.Column(db.String(16),unique=True)
    #gentime = db.Column(db.DateTime, index=True, default = datetime.utcnow)
   
    def __init__(self, pin):
        self.pin = pin
        #self.s_No = s_No

db.create_all()

