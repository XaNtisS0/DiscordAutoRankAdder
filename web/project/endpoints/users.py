from flask_restful import Resource, reqparse, abort, fields, marshal_with

from project.app import db, api
from project.models.rank import Rank
from project.models.server import Server

from project.models.user import User

user_resource_fields = {
	'id': fields.Integer,
	'server_id': fields.Integer,
	#'server': fields.String,
	'username': fields.String,
	#'ranks': fields.List
}

user_post_args = reqparse.RequestParser()
user_post_args.add_argument(
	"username", type=str, help="Name is required.", required=True)
user_post_args.add_argument(
	"ranks", type=list, help="Ranks list is required.", required=True)

user_update_args = reqparse.RequestParser()
user_update_args.add_argument("server_id", type=int)
user_update_args.add_argument("username", type=str)
user_update_args.add_argument("ranks", type=list)


class UsersEndpoint(Resource):
	@marshal_with(user_resource_fields)
	def get(self, serv_id):
		result = User.query.filter_by(server_id=serv_id).all()
		return result, 200

	def post(self, serv_id):
		args = user_post_args.parse_args()
		# server = Server.query.get(serv_id)
		user = User(server_id=serv_id, username=args['username'])
		# for rank in args['ranks']:
		# 	item = Rank(name=rank)
		# 	user.ranks.append(item)
		# server.users.append(user)
		# db.session.add(server)
		db.session.add(user)
		db.session.commit()
		for rank in args['ranks']:
			item = Rank(name=rank, user_id=user.id)
			db.session.add(item)
		db.session.commit()
		return "", 201


class UserEndpoint(Resource):
	@marshal_with(user_resource_fields)
	def patch(self, serv_id, user_id):
		args = user_update_args.parse_args()
		result = User.query.filter_by(
			id=user_id, server_id=serv_id).first()
		if not result:
			abort(404, message="User with this id does not exist.")
		for arg in args:
			if arg:
				result.arg = arg
		db.session.commit()
		return result, 200

	def delete(self, serv_id, user_id):
		result = User.query.filter_by(id=user_id, server_id=serv_id)
		if not result:
			abort(404, message="User with this id does not exist.")
		db.session.delete(result)
		return "", 200


api.add_resource(UsersEndpoint, "/<int:serv_id>/users")
api.add_resource(UserEndpoint, "/<int:serv_id>/users/<int:user_id>")