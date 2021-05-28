from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
'''configurando o banco de dados '''
db=SQLAlchemy()

def configure_db(app):
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///storage.db'
    db.init_app(app)
    # db.create_all()
    app.db=db
    print('banco de dados configurado')

