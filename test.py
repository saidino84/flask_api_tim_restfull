import requests as rq

base_url='http://127.0.0.1:5000/'

resp=rq.get(base_url+'helloworld_api') #http://127.0.0.1:5000/helloworld_api
print(resp.json())