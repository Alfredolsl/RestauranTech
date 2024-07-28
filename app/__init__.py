from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os
import time
from sqlalchemy.exc import OperationalError, PendingRollbackError
from sqlalchemy.sql import text

# Inicializar db y login_manager fuera de create_app para evitar el error de 'str' object has no attribute 'init_app'
db = SQLAlchemy()
login_manager = LoginManager()

def connect_db_with_retries(db, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            db.session.execute(text('SELECT 1'))
            break
        except OperationalError:
            retries += 1
            time.sleep(2)
    else:
        raise Exception('Could not connect to the database.')


def create_app():
    app = Flask(__name__)

    load_dotenv()
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_user = os.getenv('DB_USER')
    db_pwd = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DATABASE')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'test')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_recycle': 280
    }

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    @app.before_request
    def before_request():
        try:
            connect_db_with_retries(db)
        except PendingRollbackError:
            db.session.rollback()

    @app.teardown_request
    def teardown_request(exception=None):
        if exception:
            db.session.rollback()
        db.session.remove()

    return app

app = create_app()

# Importar las rutas después de la inicialización
from app import routes
