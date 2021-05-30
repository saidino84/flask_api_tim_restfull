from flask_restful import Resource,reqparse,abort
from app.models.videos import Video


def abort_if_videos_id_doesnt_exist(video_id):
    video=Video.query.filter_by(id=video_id).first()
    if video ==None:
        return abort(404, message='Video nao encontrado')

def abort_if_video_exists(video_id):
    # TODO IMPLEMENT IT
    videos={} 
    if video_id in videos:
        abort(404,message='video already exists with that ID')


class Video(Resource):

    def get(self,video_id):
        abort_if_videos_id_doesnt_exist(video_id)
        return Video.query.filter_by(id=video_id).first()

    def put(self,video_id):
        abort_if_video_exists(video_id)
        return 'hello'



