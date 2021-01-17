import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY", "totallyrandomkey")
app.config.from_object("project.config.Config")


db = SQLAlchemy(app)