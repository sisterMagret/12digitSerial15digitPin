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


"""instantiating the SQLAlchemy Class in db """
db=SQLAlchemy(app)

"""this API generates a random number"""
migrate = Migrate(app,db)
class Gen_pin(Resource):

    def post(self):

        """convert uuid formate to python string"""
        pin=str(uuid.uuid4())

        """convert char to uppercase"""
        pin=pin.upper()

        """remove the - in uuid """
        pin = pin.replace("-","")

        pin = pin[0:15]

        pinGen = generate(pin)
        
        """adding the pin to the database"""
        db.session.add(pinGen)

        """commiting the new added item"""
        db.session.commit()

        """querying a column by the pin and saving it to the variable result"""
        result = generate.query.filter_by(pin = pin).first()
        
        """fetching the id of the particular pin and saving in s_N"""
        s_n = result.s_No
        return {"SN":s_n, 'pin': pin }

api.add_resource(Gen_pin, '/api/generate') 
 


class Val_pin(Resource):
    def post(self):
        """instantiating the request.get_json method to enable user to enter needed information"""
        request_data = request.get_json()

        """requesting a pin from user for validation"""
        pin = request_data['pin']
        sn = request_data['sn']

        """searching for that paticular pin in the database"""
        result1 = generate.query.filter_by(pin = pin).first()
        result2 = generate.query.filter_by(s_No = sn).first()
        
        
        #if pin is found it returns 1 for success
        if result1 == result2:
            return{"response":1}

        # else if pin is not found it returns o to represent failure
        else:
            return{"response": 0}    

api.add_resource(Val_pin, '/api/validate')         
    
if __name__ == "__main__":
    app.run()