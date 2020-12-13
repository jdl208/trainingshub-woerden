from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()


def create_app():
    """
    docstring
    """
    app = Flask("__name__", static_folder="app/static", template_folder="app/templates")
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    with app.app_context():

        from app.auth.routes import bp as auth

        app.register_blueprint(auth)

        @app.route("/")
        def home():
            """
            dummy route for development
            """
            return "<a href='register'>register</a>"

        return app
