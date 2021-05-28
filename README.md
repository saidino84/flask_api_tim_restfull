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

# 3 Testando com metodo HTTP.put
```py
# app.py
videos ={}
class Video(Resource):
    def get(self,video_id):
        print('tring to get video',video_id)
        if not (str(video_id) in videos):
            return 'video nao achado'
        return videos[str(video_id)]

    def put(self,video_id):
        # requests.put(base_url+'video/1',{'likes':20})
        likes=request.form['likes'] #para obter uk foi put basta receber por request.form['nome']
        videos['likes']=likes
        return videos

api.add_resource(Video, '/video/<int:video_id>')

if __name__== "__main__":
    app.run(debug=True)

#  testando test.py
# ...
base_url='http://127.0.0.1:5000/'
def put_method():
    input('put method')
    resp3=rq.put(base_url+'video/1',{'likes':20})
    print(resp3.status_code)
    print(resp3.json())

``` 

# RETIFICANDO 
>> Veja que na parte 2 o aclasse Video(Resoure) no metodo put para receber os dados
>> ele precisou usar o request.form , 
>> com aclasse restfull_api nao precisamos disso pos ela tem um metodo
>> que é capas de n=interceptar os requests de uma forma bacana sem precisar 
>> a metodo request de Flask 
 ```py 
    from flask_restfull import Api, Resource, reqparse #[reqparse]
    # pra dizer ao request k vou receber os dados atraves do request,
    #os argumentos:['name, (k seria o name d video),
    #'views'(k seria os views do video), e 'likes' do video]
    # para pegar os dados recebido por meio de put (Resource automaticament interceptara)
    videos_put_args=reqparse.RequestParser()
    videos_put_args.add_argument('name',type=str, help='Nome do video')
    videos_put_args.add_argument('views', type=int, help='Views of the video')
    videos_put_args.add_argumenr('likes',type=int, help='Likes on the video)

    # se o sender nao mandar esses argumentos o flask vai retornar
    # o erro consoante os parametros{ en caso de 'name' sera retornado um erro dizendo: Nome do Video}

    '''
    E no método put da class Video k extende (Resource)
    '''
    def put(self,video_id):
        '''aque estou recebendo argumentos que eu quero k o cliente
        k fizer o put pra esta route, venha com eles em caso de faltar um arg dos [name,views,likes]
        '''
        args = video_put_args.parse_args()
        return {video_id:args}

# test.py
response =requests.put(base_url+'video/1', {'likes':20})
>>{'1': {'name':None,'views':None,'likes':20}}
# view k  se nao atribuirsmos os outros argumentos no put
#  o seram devolvido como None o value deles

'''
e se atribuirs os required=True pra cada arqparse ao fazermos put sem
informar alguns atributos seras devolvidos a messagem de help para os arqparses com required=True
'''
ideos_put_args.add_argument('name',type=str, help='Nome do video',required=True)
    videos_put_args.add_argument('views', type=int, help='Views of the video',required=True)
    videos_put_args.add_argument('likes',type=int, help='Likes on the video',required=True)

"test.py"
# test.py
response =requests.put(base_url+'video/1', {'likes':20})
>>{'message': {'name': 'Nome do video'}} 
# agora ele nos devolve um erro com amessage dizemdp k precisa passar
# o nome pk é required

 ``` 