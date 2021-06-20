import os
from app import create_app
#
# port=int(os.environ.get('PORT',5000))
#
# if __name__=='__main__':
#     app =create_app()
#     app.run(host='0.0.0.0',port=port)
# else:
#     gunicorn_app=create_app()

def main():
    app = create_app()
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
