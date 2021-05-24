# flask_api_tim_restfull
criacao de api com flask 

# 1 o basico de api com restifull

```py
#app.py

from flask import Flask
from flask_restful import Api, Resource


app=Flask(__name__)
api= Api(app)

class HelloWord(Resource):
    'Resource to handle get/post/delete /put  http requests'
    def get(self):
        return {"dados":"Hello World "}
 

api.add_resource(HelloWord, '/helloworld_api')

if __name__== "__main__":
    app.run(debug=True)

``` 

# Testando com requests do python

```py
'test.py'
import requests as rq

base_url='http://127.0.0.1:5000/'

resp=rq.get(base_url+'helloworld_api') #http://127.0.0.1:5000/helloworld_api
print(resp.json())
```

# 2 - Modificando o methodo get to Api passando parametro 
```py
db={
    'tim':{'idade':23,'gender':'male'},
    'saidin':{'idade':13,'gender':'male'}
    }
class HelloWord(Resource):
    'Resource to handle get/post/delete /put  http requests'
    def get(self, name,idade):
        return  db[name]
api.add_resource(HelloWord, '/helloworld/<string:name>/<int:idade>')


    
"Na requisicao vai mudar tambem :
import requests as rq

base_url='http://127.0.0.1:5000/'

resp=rq.get(base_url+'helloworld_api/saidino/23') #http://127.0.0.1:5000/helloworld_api
print(resp.json())
">> {os dados de saidino}"


```