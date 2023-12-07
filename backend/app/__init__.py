from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import BadRequest

from app.config import DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()

# create the application object
def create_app():
    app = Flask(__name__)

    # use Development Config
    config = DevelopmentConfig
    app.config.from_object(config)

    CORS(app)

    # Initialize Database Plugin
    db.init_app(app)
    migrate.init_app(app, db)

    
    from app.models import Student
    with app.app_context():
        db.create_all()

    register_blueprints(app)
    # create_database(app)

    return app
    


# Register all blueprints
def register_blueprints(app):

    from app.api.student_request import student_request

    app.register_blueprint(student_request)

# creates database models
def create_database(app):
    from app.api import Student
    with app.app_context():
        db.create_all()

# Register error Handlers
def register_error_handlers(app):
    app.register_error_handler(BadRequest, handle_bad_request_error)


def handle_bad_request_error():
    return {"success:": False, "message": get_text("status_codes.404")}, 404



