from flask import Flask
from flask_login import LoginManager
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

login = LoginManager()
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    login.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)

    from .articles import articles as articles_blueprint
    app.register_blueprint(articles_blueprint)

    return app
    
