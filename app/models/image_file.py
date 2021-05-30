import  os
from base64 import b64encode
import base64
from io import BytesIO #convert data from Database into bytes


from app.db import db
from datetime import datetime

class ImageModel(db.Model):
    '''
    image baixavel

    '''
    id   = db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String(128), nullable=False)
    data =db.Column(db.LargeBinary, nullable=False) #Actual data, needed for doenload
    rendered_data =db.Column(db.Text, nullable=False)#data to render the pic in browser
    text =db.Column(db.Text)
    location = db.Column(db.String(64))
    pic_date =db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self):
        return f' Pic Name:{self.name} text:{self.text} created_ on {self.pic_date} location:{self.location}'
