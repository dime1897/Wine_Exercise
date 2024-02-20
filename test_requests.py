import requests

url="https://exercises-00.nw.r.appspot.com/api/v1"

body = {
            'label': {
                'name': 'Collection 1985',
                'type': 'sparkling',
                'producer': 'Krug',
                'year': 1985,
                'price': 1945.00
            },
            'quantity': 10,
            'minimum': 6
        }
print("GET: "+url+"/clean")
resp = requests.get(url+'/clean')
print(str(resp) + ":" + resp.text)
print('\n\n')

print("POST: "+url+"/slot/4\nBODY: "+ str(body))
resp = requests.post(url+'/slot/4', json= body)
print(str(resp) + ":" + resp.text)
print('\n\n')

body = {
            'label': {
                'name': 'Sassicaia Bolgheri',
                'type': 'red',
                'producer': 'Tenuta San Guido',
                'year': 2010,
                'price': 850
            },
            'quantity': 8,
            'minimum': 3
        }
print("POST: "+url+"/slot/2\nBODY: "+ str(body))
resp = requests.post(url+'/slot/2', json= body)
print(str(resp) + ":" + resp.text)
print('\n\n')

print("POST: "+url+"/slot/2\nBODY: "+ str(body))
resp = requests.post(url+'/slot/2', json= body)
print(str(resp) + ":" + resp.text)
print('\n\n')

print("POST: "+url+"/slot/3\nBODY: "+ str(body))
resp = requests.post(url+'/slot/3', json= body['label'])
print(str(resp) + ":" + resp.text)
print('\n\n')

body = {
            'label': {
                'name': 'San Giovese',
                'type': 'red',
                'producer': 'Casa Mia',
                'year': 2020,
                'price': 13.5
            },
            'quantity': 9,
            'minimum': 5
        }
print("POST: "+url+"/slot/0\nBODY: "+ str(body))
resp = requests.post(url+'/slot/0', json= body)
print(str(resp) + ":" + resp.text)
print('\n\n')

body = {
            'label': {
                'name': 'Lambrusco',
                'type': 'red',
                'producer': 'Azienda Agricola Bompastore',
                'year': 2021,
                'price': 15.6
            },
            'quantity': 14,
            'minimum': 8
        }
print("POST: "+url+"/slot/1\nBODY: "+ str(body))
resp = requests.post(url+'/slot/1', json= body)
print(str(resp) + ":" + resp.text)
print('\n\n')

body = {
            'label': {
                'name': 'Pinot Grigio',
                'type': 'white',
                'producer': 'Casa di Fillo',
                'year': 2010,
                'price': 120
            },
            'quantity': 6,
            'minimum': 3
        }
print("POST: "+url+"/slot/7\nBODY: "+ str(body))
resp = requests.post(url+'/slot/7', json= body)
print(str(resp) + ":" + resp.text)
print('\n\n')

body = {
            'label': {
                'name': 'Malvasia',
                'type': 'sweet',
                'producer': 'Rossetto snc',
                'year': 2017,
                'price': 20
            },
            'quantity': 11,
            'minimum': 7
        }
print("POST: "+url+"/slot/9\nBODY: "+ str(body))
resp = requests.post(url+'/slot/9', json= body)
print(str(resp) + ":" + resp.text)
print('\n\n')

print("GET: "+url+"/slot/4")
resp = requests.get(url+'/slot/4')
print(str(resp) + ":" + resp.text)
print('\n\n')

print("GET: "+url+"/slot/2")
resp = requests.get(url+'/slot/2')
print(str(resp) + ":" + resp.text)
print('\n\n')

print("GET: "+url+"/slot/3")
resp = requests.get(url+'/slot/2')
print(str(resp) + ":" + resp.text)
print('\n\n')

