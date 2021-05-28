from flask_marshmallow import Marshmallow
from .videos import Video

ma =Marshmallow()

def configure_ma(app):
    'configurando o serializador'
    ma.init_app(app)
    print('marshmallow has sucessfull configured')


class VideoShema(ma.Schema):

    class Meta:
        # os campos a serem devolvidos do banco de dados
        fields = ('id','name','likes','views')


video_schema = VideoShema()
videos_schema = VideoShema(many=True)  #ou fazer query de tods Video.query.all() [{},{},{}]

'''
ex:
video1=Video.query.filter_by(id=1).first()
json_v=video_schema.dump(video1)

varios videos:
return videos_schema.dump(Video.query.all())


'''