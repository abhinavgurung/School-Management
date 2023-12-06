from flask import Flask
from flask_cors import CORS


# create the application object
def create_app():
    app = Flask(__name__)

    CORS(app)

    register_blueprints(app)

    return app
    


# Register all blueprints
def register_blueprints(app):

    from app.api.student_request import student_request

    app.register_blueprint(student_request)

