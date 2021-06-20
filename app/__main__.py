from flask import Flask,request,Response,render_template,url_for
from app.db import configure_db
from flask_migrate import Migrate
from app.models.image_file import ImageModel,ImageTeste
import os




def create_app():

    app=Flask(__name__,template_folder='templates', static_folder='static')
    app.secret_key=os.urandom(23)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    configure_db(app)



    # from app.models.videos import Video
    from app.models.serializer import configure_ma

    # configuracao de marshmallow
    configure_ma(app)

    # config db
    Migrate(app,app.db)

    # from app.controllers.videos.views import configure_video_bp
    from app.api import create_api

    api=create_api(app)

    # app.register_blueprint(videos_bp, url_prefix='/videos')

    # todo CONFIGURANDO VIDEO API
    # configure_video_bp(app)


    # from app.models.videos import Video
    from app.models.image_m_api import ImageModelApi

    from app.controllers.image_saver import  configure_img_bp
    from app.controllers import config_bp_img_test

    @app.route("/")
    def index():
        print('The homePage')
        return 'Hello the first page'
    configure_img_bp(app)
    config_bp_img_test(app)

    @app.shell_context_processor
    def make_shell_context():
        # com isto aki posso entrar no shell e fazer testes esporatico
        '''
        db.create_all()  >> criare o banco


        '''
        return dict(app=app,db=app.db,Image=ImageModelApi, ImgText=ImageTeste)
    return app








if __name__=='__main__':
    create_app().run(debug=True,host='0.0.0.0', port=5000)
