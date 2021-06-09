from app.db import db


class ImageModelApi(db.Model):
    ''' Tabel de ImageApi'''
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    title=db.Column(db.String, nullable=False)
    description=db.Column(db.Text,nullable=False)
    imageUrl=db.Column(db.Text(255))
    likes=db.Column(db.Integer,)
    views=db.Column(db.Integer)
    is_favorite=db.Column(db.Boolean, nullable=False)


    def __init__(self,title,description, imageUrl,likes=0,views=0,is_favorite=False ):
        self.title=title
        self.description=description
        self.imageUrl=imageUrl
        self.likes=likes
        self.views=views
        self.is_favorite=is_favorite

    
    def __repr__(self):
        return f'<ImageModelApi : {self.title} , is_favorite: {self.is_favorite}, likes:{self.likes} image_url:{self.imageUrl}'






"""

final int id;
  final String imageUrl;
  final String title;
  final String description;
  final int likes;
  final int views;
  final bool favorite;
"""



from app.db import db



class Video(db.Model):
    id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    name=db.Column(db.String(200), nullable=False)
    views=db.Column(db.Integer, nullable=False)
    likes=db.Column(db.Integer, nullable=False)
    image=db.Column(db.String(255),)

    def __init__(self, name,image,likes=0,views=0,**kwargs):
        super(Video,self).__init__(**kwargs)
        self.name = name
        self.likes=likes
        self.views=views
        self.image=image


    def __repr__(self,):
        return f'<Video: Video Name{self.name} >'