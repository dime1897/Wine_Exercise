from google.cloud import firestore
from google.cloud.firestore_v1.base_query import FieldFilter
import time

db = firestore.Client(database="wine")

def decrease_quantity(request) -> None:
        label = request.get_json().get('label')
        wines_ref = db.collection('wines')
        doc = wines_ref.where(filter = FieldFilter("label", "==", label)).stream()
        wine={}
        doc_id=-1
        for d in doc:
             wine = d.to_dict()
             doc_id = str(d.id)
        print(wine) 
        wine['quantity'] -= 1
        print('Decreased')
        if wine['quantity'] < wine['minimum']:
                order = {
                       'label': wine['label'],
                       'quantity_ordered': 6
                }
                db.collection('orders').document(str(time.time())).set(order)
        wines_ref.document(doc_id).update(wine)

#if __name__ == '__main__':
#        decrease_quantity({
#                'name': 'Lambrusco',
#                'type': 'red',
#                'producer': 'Azienda Agricola Bompastore',
#                'year': 2021,
#                'price': 15.6
#            })