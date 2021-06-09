from flask_restful import Api
# from app.api.video_api import Video
from app.api.image_api import   ImageApi

def create_api(app):
    api=Api(app)
    app.api=api
    # api.add_resource(Video, '/videos/<int:video_id>')
    api.add_resource(ImageApi, '/imageapi/<int:image_id>')



'''
todo Outras formas de inicializar uma api
def init_app(self, app):
    Initialize this class with the given :class:`flask.Flask`
    application or :class:`flask.Blueprint` object.

    :param app: the Flask application or blueprint object
    :type app: flask.Flask
    :type app: flask.Blueprint
Examples::
    api = Api()
    api.add_resource(...)
    api.init_app(app)
'''