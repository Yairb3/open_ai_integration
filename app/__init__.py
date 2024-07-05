import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@db:5432/postgres'#os.environ.get('DATABASE_URI')
    if not app.config['SQLALCHEMY_DATABASE_URI']:
        raise KeyError ("Here is error")
    return app

def init_db(app):
    db = SQLAlchemy(app)
    with app.app_context():
        db.create_all()
    return db