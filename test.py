import requests as rq

base_url='http://127.0.0.1:5000/'
input('base_url,  start requests?')

def basic_get():
    resp=rq.get(base_url+'helloworld_api') #http://127.0.0.1:5000/helloworld_api
    print(resp.json())
def requ2():
    input('get method 2')
    resp2=rq.get(base_url+'video/2')
    print(resp2.json())

def put_method():
    '''
    EX1: sem required=True esta metodo passa

    '''
    input("put method exemplo d \n metodo= resp3=rq.put(base_url+'video/1',{'likes':20}) ")
    resp3=rq.put(base_url+'video/1',{'likes':20})
    print(resp3.status_code)
    print(resp3.json())
def put_method_ex2():
    id=input('whast is id')
    input("put method exemplo d \n metodo= resp3=rq.put(base_url+'video/1',{'likes':20}) ")
    resp3=rq.put(base_url+f'video/{id}',{'likes':20,'name':'coronavirus','views':10})
    print(resp3.status_code)
    print(resp3.json())

# put_method()
# put_method_ex2()
input()
requ2()
def get_all():
    again=1
    while again !=0:
        id=int(input('id>>'))
        res=rq.get(base_url+f'video/{id}')
        print(res.json())
        again=int(input('again?'))
        

def put_many(time):

    for i in range(time):
        data={'name':input('name'),
       'views':int(input('views')),
        'likes':int(input('likes'))}
        resp=rq.put(base_url+f'video/{i}',data)
        # print(resp.json())
        if 'n' in input('again ?').lower():
            ...
        else:
            break
        print('THATS A RESPONSE RESULT')
        print(resp.json())
def delete_many():
    more=True
    while more:
        id=int(input(' type id of video type=int'))
        try:
            resp=rq.delete(base_url+"video/id")
            print(f'{resp} ====DELETED')
        except Exception as e :
            print(f'error deletind   {e}')
        else:
            more=bool(input('delete  again?'))



input('put many')
put_many(int(input('times')))

input('gat_all')
get_all()
delete_many()


