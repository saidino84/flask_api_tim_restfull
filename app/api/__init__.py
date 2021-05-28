from flask_restful import Api
from app.api.video_api import Video

def create_api(app):
    api=Api(app)
    app.api=api

    api.add_resource(Video, '/videos/<int:video_id>')