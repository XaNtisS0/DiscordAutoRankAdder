import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from .config import Config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY", "totallyrandomkey")
app.config.from_object(Config)

api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
