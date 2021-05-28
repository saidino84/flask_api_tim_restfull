from flask import Flask,request
from flask_restful import Api, Resource,reqparse,abort


def create_app():
    app=Flask(__name__)
    api= Api(app)



class HelloWord(Resource):
    'Resource to handle get/post/delete /put  http requests'
    def get(self):
        return {"dados":"Hello World "}

    def post(self):
        return {'data':'posted'}

api.add_resource(HelloWord, '/helloworld_api')


# Exemplo 2 APi de Videos 
videos ={}

videos_put_args=reqparse.RequestParser()
videos_put_args.add_argument('name',type=str, help='Nome do video is required', required=True)
videos_put_args.add_argument('views', type=int, help='Views of the video is required',required=True)
videos_put_args.add_argument('likes',type=int, help='Likes on the video is required ',required=True)

def abort_id_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404,message=f'O video com id {video_id} Nao existe')

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(404,message='video already exists with that ID')


class Video(Resource):
    def get(self,video_id):
        abort_id_video_id_doesnt_exist(video_id)
        print(f'============== [videos] {videos}===================')
        print('tring to get video',video_id)

        if not (video_id in videos):
            return 'video nao achado'
        return videos[video_id]

    def put(self,video_id):
        abort_if_video_exists(video_id)
        '''to make put to get sucessfull please have to mention:
        import requests as rq
        resp3=rq.put(base_url+'video/1',{'likes':20,'name':'coronavirus','views':10})
        print(resp3.status_code)
        print(resp3.json())

        '''
        args = videos_put_args.parse_args()
        videos[video_id]=args
        return videos,201
    
    def delete(self,video_id):
        abort_id_video_id_doesnt_exist(video_id)
        print(videos)
        del videos[video_id]
        print(f'AFTER DELETED {videos}')
        return '',204 #quando é delete o retorno é str blank

    

api.add_resource(Video, '/video/<int:video_id>')

if __name__== "__main__":
    app.run(debug=True)