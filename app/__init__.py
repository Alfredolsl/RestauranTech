""" __init__ file that contains Flask instance """
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os


def create_app():
    app = Flask(__name__)
    
    load_dotenv()
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_user = os.getenv('DB_USER')
    db_pwd = os.getenv('DB_PASSWORD')
    db = os.getenv('DATABASE')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db}'
    app.config['SECRET_KEY'] = 'test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app

app = create_app()
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from . import routes