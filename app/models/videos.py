from app.db import db



class Video(db.Model):
    id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    name=db.Column(db.String(200), nullable=False)
    views=db.Column(db.Integer, nullable=False)
    likes=db.Column(db.Integer, nullable=False)

    def __init__(self, name,likes=0,views=0,**kwargs):
        super(Video,self).__init__(**kwargs)
        self.name = name
        self.likes=likes
        self.views=views


    def __repr__(self,):
        return f'<Video: Video Name{self.name} >'

    
    
