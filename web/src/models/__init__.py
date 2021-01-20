from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .server import Server
from .user import User
from .rank import Rank