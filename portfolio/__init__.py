from flask import Flask 

def create_app(): 
    app = Flask(__name__)

    @app.route('/')
    def hello(): 
        return 'This is my Porfolio!'

    #regitster the project blueprint
    from . import project
    app.register_blueprint(project.bp)

    return app
