from flask import Flask
from flask_restful import Api, Resource


app=Flask(__name__)
api= Api(app)

class HelloWord(Resource):
    'Resource to handle get/post/delete /put  http requests'
    def get(self):
        return {"dados":"Hello World "}

    def post(self):
        return {'data':'posted'}

api.add_resource(HelloWord, '/helloworld_api')

if __name__== "__main__":
    app.run(debug=True)