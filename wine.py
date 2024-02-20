from google.cloud import firestore


class Wine(object):
    def __init__(self) -> None:
        self.db = firestore.Client(database="wine")
    
    def clean_db(self) -> None:
        wines_ref = self.db.collection('wines')
        orders_ref = self.db.collection('orders')
        try:
            for slot in wines_ref.list_documents():
                slot.delete()     
            for order in orders_ref.list_documents():
                order.delete()
        except Exception as e:
            print("Exception cought in clean_db(): \n {" + str(e) + "}")

    def insert_slot(self, slot_details:dict, slot:str) -> dict:
        wines_ref = self.db.collection('wines')
        try:
            wines_ref.document(slot).set(slot_details)
            return slot_details['label']
        except Exception as e:
            print("Exception cought in insert_slot(): \n {" + str(e) + "}")
            return None
        
    def get_slot(self, slot:str) -> dict:
        wines_ref = self.db.collection('wines')
        try:
            slot_doc = wines_ref.document(slot).get()
            slot_details = slot_doc.to_dict() if slot_doc.exists else None
            return slot_details
        except Exception as e:
            print("Exception cought in get_slot(): \n {" + str(e) + "}")
            return None
        
    def get_label_list(self):
        wines_ref = self.db.collection('wines')
        try:
            docs = wines_ref.stream()
            spum_list = []
            white_list = []
            red_list = []
            sweet_list = []
            for doc in docs:
                d = doc.to_dict()
                if d['label']['type'] == 'sparkling': spum_list.append({'name': d['label']['name'], 'price': d['label']['price'], 'quantity': d['quantity']})
                if d['label']['type'] == 'white': white_list.append({'name': d['label']['name'], 'price': d['label']['price'], 'quantity': d['quantity']})
                if d['label']['type'] == 'red': red_list.append({'name': d['label']['name'], 'price': d['label']['price'], 'quantity': d['quantity']})
                if d['label']['type'] == 'sweet': sweet_list.append({'name': d['label']['name'], 'price': d['label']['price'], 'quantity': d['quantity']})
            return spum_list, white_list, red_list, sweet_list
        except Exception as e:
            print("Exception cought in get_label_list(): \n {" + str(e) + "}")
            return None, None, None, None

#if __name__ == '__main__':
#    dao = Wine()
#    s, w, r, sw = dao.get_label_list()
#    print(s)
#    print(w)
#    print(r)
#    print(sw)
#
#    dao.insert_slot(
#        {
#            'label': {
#                'name': 'Collection 1985',
#                'type': 'sparkling',
#                'producer': 'Krug',
#                'year': 1985,
#                'price': 1945.00
#            },
#            'quantity': 10,
#            'minimum': 6
#        }, '4'
#    )
#
#    dao.insert_slot(
#        {
#            'label': {
#                'name': 'Sassicaia Bolgheri',
#                'type': 'red',
#                'producer': 'Tenuta San Guido',
#                'year': 2010,
#                'price': 850
#            },
#            'quantity': 8,
#            'minimum': 3
#        }, '2'
#    )
#
#    print(dao.get_slot('4'))
#    print("\n\n\n")
#    print(dao.get_slot('3'))
#    print("\n\n\n")
#    print(dao.get_slot('2'))