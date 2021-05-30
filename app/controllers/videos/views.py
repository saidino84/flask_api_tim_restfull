from flask import Blueprint,jsonify, render_template
from app.models.videos import Video
from app.models.serializer import videos_schema,video_schema

videos_bp=Blueprint('video',__name__,static_folder='static',template_folder='templates')

@videos_bp.route('/')
@videos_bp.route('/get_all_videos')
def get_all():
    
    print('routa de videos por meio de views')
    videos=Video.query.all()
    # print(videos)
    videos_json=videos_schema.dump(videos)
    print(videos_json)

    return jsonify(videos_json)

@videos_bp.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@videos_bp.route('/get_video_by_id/<id>')
def get_video_by_id(id):
    try:
        video=Video.get(id)
        video_json=videos_schema.dump(video)
        return video_json
    except  Exception as e:
        return jsonify({'erro':"user_not_found"})
    return 'error'

def configure_video_bp(app):
    app.register_blueprint(videos_bp, url_prefix='/video')
    print('Video blue_print configured sucess')