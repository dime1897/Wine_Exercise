from flask import Flask, render_template, request
from flask_restful import Resource, Api
from wtforms import Form, IntegerField, StringField, validators, SubmitField
from wine import Wine

app = Flask(__name__,
            static_url_path='/static', 
            static_folder='static')
dao=Wine()

api = Api(app)
basePath = '/api/v1'
label_fields=['name', 'price', 'producer', 'type', 'year']
slot_fields=['label', 'minimum', 'quantity']
types = ['sparkling', 'white', 'red', 'sweet']

def validate_slot_number(slot:str) -> bool:
    try:
        if int(slot) < 0 or int(slot) > 9:
            return False
        return True
    except:
        #Means that slot is not a number
        return False
    
def validate_slot(slot_details:dict) -> bool:
    try:
        if len(slot_details.keys()) != len(slot_fields): return False #Too much fields
        for key in slot_details.keys():
            if not key in slot_fields: return False #Field not compliant
        #Now we are sure all fields are correct, let's check for values
        if slot_details['quantity'] < slot_details['minimum'] or slot_details['quantity'] < 6 or slot_details['quantity'] > 14 or slot_details['minimum'] < 3 or slot_details['minimum'] > 8: return False        
        label = slot_details['label']
        if len(label.keys()) != len(label_fields): return False #Too much fields
        for key in label.keys():
            if not key in label_fields: return False #Field not compliant
        if label['year'] < 1900 or label['year'] > 2021 or label['price'] < 0 or not label['type'] in types: return False
        return True
    except:
        #Something is not what it should be
        return False

class Wine_Handling(Resource):
    def get(self, slot):
        if not validate_slot_number(slot): return None, 404
        slot = dao.get_slot(slot)
        if slot is None: return None, 404
        else: return slot, 200

    def post(self, slot):
        if not validate_slot_number(slot): return None, 400
        slot_details = request.json
        if not validate_slot(slot_details): return None, 400
        conflict = dao.get_slot(slot)
        if not conflict is None: return None, 409
        ret = dao.insert_slot(slot_details, slot)
        if ret is None: return None, 400
        else: return ret, 201

class Wine_Clean(Resource):
    def get(self):
        dao.clean_db()
        return None, 200

@app.route(f'{basePath}/wine_card', methods=['GET'])
def wine_card():
    spum, white, red, sweet = dao.get_label_list()
    return render_template('wine_card.html', spum=spum, white=white, red=red, sweet=sweet), 200

api.add_resource(Wine_Handling, f'{basePath}/slot/<slot>')
api.add_resource(Wine_Clean, f'{basePath}/clean')

if __name__ == '__main__':
    app.run()
