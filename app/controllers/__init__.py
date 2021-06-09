from flask import Blueprint,render_template,Response,request, redirect, url_for
from app.db import db
from app.models.image_file import   ImageTeste
from werkzeug.utils import secure_filename

img=Blueprint('im_test',__name__,url_prefix='/img_test')

def config_bp_img_test(app):
    app.register_blueprint(img)
    print('IMage test config sucessfull')

@img.route('/start')
def image_index():
    imgs=ImageTeste.query.all()
    return render_template('image_db_test.html', images=imgs)
@img.route('/upload', methods=['POST'])
def upload_test():
    pic= request.files['pic']
    if not pic:
        return '<h4>Nenhuma image post <a href="/img_test/upload"> Volte a afazer upload de novo</a></h4>'
    
    filename=secure_filename(pic.filename)
    mimetype =pic.mimetype

    img =ImageTeste(img=pic.read(),mime_type=mimetype,name=filename)
    db.session.add(img)
    db.session.commit()

    return render_template('/img_test/start')

@img.route('/<int:id>', methods=['GET', ])
def get_image(id):
    img=ImageTeste.query.filter_by(id=id).first()
    if not img:
        return f'NO image with that {id}'
    print('Image found ')
    image=img.img
    return Response(img.img, mimetype=img.mime_type)
    # return f'<p>IMage</p> <img src={Response(img.img, mimetype=img.mime_type)}><img/>'

