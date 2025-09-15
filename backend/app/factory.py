from flask import Flask
from app.config import config
from app.extensions import db, migrate, cors
from app.api.v1.routes import register_blueprints

def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_blueprints(app)

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    return app