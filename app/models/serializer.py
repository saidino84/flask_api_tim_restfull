from flask_marshmallow import Marshmallow
# from .videos import Video
from .image_file import ImageModel

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


class ImageSchema(ma.Schema):
    class Meta:
        fields=['id','name','text','data']
   

image_schema =ImageSchema()
images_schema=ImageSchema(many=True)
'''
ex:
video1=Video.query.filter_by(id=1).first()
json_v=video_schema.dump(video1)

varios videos:
return videos_schema.dump(Video.query.all())




 id   = db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String(128), nullable=False)
    data =db.Column(db.LargeBinary, nullable=False) #Actual data, needed for doenload
    rendered_data =db.Column(db.Text, nullable=False)#data to render the pic in browser
    text =db.Column(db.Text)
    location = db.Column(db.String(64))
    pic_date =db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


use this for SQLAlchema Schemas

    class AuthorSchema(ma.SQLAlchemySchema):
        class Meta:
        model = Author

    id = ma.auto_field()
    name = ma.auto_field()
    books = ma.auto_field()


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        include_fk = True

'''