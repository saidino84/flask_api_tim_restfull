from base64 import b64encode
import base64
from io import BytesIO #convert data from Database into bytes


from app.db import db
from datetime import datetime
from flask import Blueprint,request, render_template, flash,redirect, url_for,jsonify
from app.models.image_file import ImageModel
from werkzeug.utils import secure_filename

from app.models.serializer import images_schema

img_bp=Blueprint('image',__name__, static_folder='static',template_folder='templates',)


def render_picture(data):
    """ takes the bytes raw version of the pic and return 
    decodede version , so that it can be used to display on the web
    """
    render_pic =base64.b64encode(data).decode('ascii')
    return render_pic
def read_image(data):
    read=base64.b64decode(data)

    with open('image.png','w') as i:
        i.write(read)
    return i 



@img_bp.route("/index", methods=['GET', 'POST'])
@img_bp.route('/')
def index():
    '# Index It routes to index.html where the upload forms is '
    flash(u'Well come !',category='error')

    _images=ImageModel.query.all()
    # image=_images[0]
    # img=read_image(image.rendered_data)
    arquivo=url_for('static',filename='arquivo.txt')
    with open(arquivo, 'r+') as file:
        print(file.read())
        from time import sleep
        sleep(2)

    return render_template('index.html', images=_images, base64=base64)
@img_bp.route('/render')
def render():
    return render_template('upload.html')

@img_bp.route('/upload', methods=['POST','GET'] )
def upload():
    'route of uploader...'
    file =request.files['inputFile']
    data = file.read()
    # print(data)
    # flash(f'File name :{file.filename}')
    # return redirect(request.url)

    render_file =render_picture(data)
    text = request.form['text']

    location =request.form['location']
    

    new_file=ImageModel(name=secure_filename(file.filename), data=data,rendered_data=render_file, text=text, location=location)
    db.session.add(new_file)
    db.session.commit()

    flash(f'Pic {new_file.name}  Uploaded Text: {new_file.text}  LOcation:{new_file.location}')
    return render_template('index.html')

@img_bp.route('/get_image_api',methods=['GET', ])
def get_images_api():
    images =ImageModel.query.all()
    return jsonify(images_schema.dump(images))

@img_bp.route('/test')
def test():
    return jsonify({'nome':'saidino'});


def configure_img_bp(app):
    app.register_blueprint(img_bp, url_prefix='/image')
    print('Image blue_print configured sucessfully')
