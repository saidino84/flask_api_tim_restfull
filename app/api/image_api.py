from flask_restful import Resource,reqparse,abort, fields,marshal_with
from flask import jsonify,current_app,url_for,redirect
from app.models.image_m_api import ImageModelApi
from app.db import db



"""
ImageModel db.Columns

self.title=title
self.description=description
self.imageUrl=imageUrl
self.likes=likes
self.views=views
self.is_favorite=is_favorite
"""
resource_fields={'id':fields.Integer, 
    'title':fields.String,
    'imageUrl':fields.String,
    'likes':fields.Integer,
    'views':fields.Integer,
    'is_favorite':fields.Boolean,
    'description':fields.String,
    }
image_put_args =reqparse.RequestParser()
image_put_args.add_argument('title',     type=str,help='Titulo da Image',required=True)
image_put_args.add_argument('likes',     type=int,help='Campo de likes da image',required=True)
image_put_args.add_argument('views',     type=int,help='Campo de views da Image',required=True)
image_put_args.add_argument('imageUrl',  type=str,help='link da image ', required=True)
image_put_args.add_argument('is_favorite',type=bool,help='campo is vaforite', required=True)
image_put_args.add_argument('description',type=str,help='campo de description of this image',required=True )

image_update_args =reqparse.RequestParser()
image_update_args.add_argument('title',     type=str,help='Titulo da Image',)
image_update_args.add_argument('likes',     type=int,help='Campo de likes da image')
image_update_args.add_argument('views',     type=int,help='Campo de views da Image' )
image_update_args.add_argument('imageUrl',  type=str,help='link da image ')
image_update_args.add_argument('is_favorite',type=bool,help='campo is vaforite' )
image_update_args.add_argument('description',type=str,help='image description update field' )

class  ImageApi(Resource):
    @marshal_with(resource_fields)
    def get(self,image_id):
        
        image=ImageModelApi.query.filter_by(id=image_id).first()
        if not image:
            abort(405, message='Nao tem video com esses ai')
        return ImageModelApi.query.all()#image

    @marshal_with(resource_fields)
    def put(self,image_id):
        video_args=image_put_args.parse_args()
        print('tentando Pegar  uma image com id {image_id}')
        result =ImageModelApi.query.filter_by(id=image_id).first()
        print('image pegue com sucesso ' if result else 'Image nao encontrado com esse id')
        if result:
            abort(409, message='Image with this  id has taken')
        
        image = ImageModelApi(title=video_args['title'],imageUrl=video_args['imageUrl'],likes=video_args['likes'],views=video_args['views'],is_favorite=video_args['is_favorite'],description=video_args['description'])
        db.session.add(image)
        db.session.commit()
        return image

    @marshal_with(resource_fields)
    def patch(self,image_id):
        args=image_update_args.parse_args()
        result =ImageModelApi.query.filter_by(id=image_id).first()
        print('image found tryng to update 'if result else 'image not foud with id so cannot be updated ')
        if not result:
            abort(404,message='Nao é posiivel fazer actualizacao de image inexistente')
        if args['title']:
            result.title=args['title']
        if args['imageUrl']:
            result.imageUrl=args['imageUrl']
        if args['views']:
            result.views=args['views']
        if args['likes']:
            result.likes=args['likes']
        if args['is_favorite']:
            result.is_favorite=args['is_favorite']
        if args['description']:
            result.description=args['description']
        print(args)
        db.session.commit()
        print('Update sucessfull')
        return result
    def delete(self,image_id):
        image =ImageModelApi.query.filter_by(id=image_id).first()
        print(current_app.db)
        if not image:
            abort(405, message='Nenhuma image com esse id :{image_id}')
        db.session.delete(image)
        db.session.commit()
        return jsonify({'action':'deleted sucessfull','response':200} ),200
    def get_all(self,image_id):
        images=ImageModelApi.query.all()
    


