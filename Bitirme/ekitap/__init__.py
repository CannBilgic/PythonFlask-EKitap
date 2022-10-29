from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def createApp():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/ekitap'
    db.init_app(app)
    return app
