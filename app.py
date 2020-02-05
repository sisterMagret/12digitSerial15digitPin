from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import uuid
from flask import Flask,request
from model import generate
from flask_migrate import Migrate



app = Flask(__name__)
api = Api(app)

"""configurations """
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///generate.sqlite3"
app.config['SECRET_KEY'] = "ABCD 12345"
app.config['SQLALCHEMY_TACK_MODIFICATIONS'] = False

"""instantiating the SQLAlchemy Class in db """
db=SQLAlchemy(app)

"""this API generates a random number"""
migrate = Migrate(app,db)
class Gen_pin(Resource):

    def get(self):

        """generates pins and convert uuid formate to python string"""
        pin = str(int(uuid.uuid4()))[:15]

        """generates serial numbers and convert uuid formate to python string"""
        s_No = str(int(uuid.uuid1()))[:12]
       
        

        pinGen = generate(pin,s_No)
        
        """adding the pin to the database"""
        db.session.add(pinGen)

        """commiting the new added item"""
        db.session.commit()

        """querying a column by the pin and saving it to the variable result"""
        result = generate.query.filter_by(pin = pin).first()
        result2 = generate.query.filter_by(s_No = s_No).first()
        
        """fetching the id of the particular pin and saving in s_N"""
        s_n = result.s_No
        return {"SN":s_n, 'pin': pin }

api.add_resource(Gen_pin, '/api/generate') 
 


class Val_pin(Resource):
    def get(self,pin):
        # checks if pin is of valid length(15) before query
        if len(pin) < 15 or len(pin) > 15:
            return f"{pin} is an invalid pin length check and try again"

        #searching for that paticular pin in the database
        result1 = generate.query.filter_by(pin = pin).first()
        
        #if pin is found it returns success message
        if result1 :
            return f"valid Pin"

        # else if pin is not found it returns a faliure message
        else:
            return f"{pin} is not a valid pin"    

api.add_resource(Val_pin, '/api/validate/<string:pin>')         
    
if __name__ == "__main__":
    app.run()