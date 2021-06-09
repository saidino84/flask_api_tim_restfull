from app.db import db



class Videos(db.Model):
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

    
    
