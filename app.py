import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.managers.db_manager import DBManager
from app.managers.openai_manager import OpenAIManager
from app.routes.routes import configure_routes

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    if not app.config['SQLALCHEMY_DATABASE_URI']:
        raise KeyError ("SQLALCHEMY_DATABASE_URI is missing")
    return app

def init_db(app):
    db = SQLAlchemy(app)
    with app.app_context():
        db.create_all()
    return db

def start_app():
    app = Flask(__name__)
    app = create_app()
    db = init_db(app)
    db_manager: DBManager = DBManager()
    openai_manager: OpenAIManager = OpenAIManager()
    configure_routes(app, db, db_manager, openai_manager)
    return app

if __name__ == '__main__':
    app = start_app()
    app.run(host="0.0.0.0", port=5000)