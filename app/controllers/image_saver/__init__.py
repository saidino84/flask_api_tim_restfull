from base64 import b64encode
import base64
from io import BytesIO #convert data from Database into bytes


from app.db import db
from datetime import datetime
from flask import Blueprint,request, render_template
from app.models.image_file import ImageModel

img_bp=Blueprint('image',__name__, static_folder='static',template_folder='templates',)


def render_picture(data):
    """ takes the bytes raw version of the pic and return 
    decodede version , so that it can be used to display on the web
    """
    render_pic =base64.b64encode(data).decode('ascii')
    return render_pic


@img_bp.route("/index", methods=['GET', 'POST'])
@img_bp.route('/')
def index():
    '# Index It routes to index.html where the upload forms is '
    return render_template('index.html')

@img_bp.route('/upload', methods=['POST','GET'] )
def upload():
    'route of uploader...'
    file =request.files['inputFile']
    data = file.read()
    print(data)
    return {'dados':data}
    render_file =render_picture(data)
    text = request.form['text']

    location =request.form['location']

    new_file=ImageFile(name=file.file_name, data=data,render_data=render_file, text=text, location=location)
    db.session.add(new_file)
    db.session.commit()

    flash(f'Pic {new_file.name}  Uploaded Text: {new_file.text}  LOcation:{new_file.locatiom}')
    return render_template('upload.html')


def configure_img_bp(app):
    app.register_blueprint(img_bp, url_prefix='/image')
    print('Image blue_print configured sucessfully')
