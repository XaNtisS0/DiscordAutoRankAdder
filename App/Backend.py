from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

db.init_app(app)

class UserModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	rank = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Video(name = {UserModel.name}, rank = {UserModel.rank})"

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of user is required", required=True)
video_put_args.add_argument("rank", type=int, help="rank of user", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of user is required")
video_update_args.add_argument("rank", type=int, help="rank of user")

resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'rank': fields.Integer,
}