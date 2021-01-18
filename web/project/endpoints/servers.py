from flask_restful import Resource, reqparse, abort, fields, marshal_with

from project.app import db, api

from project.models.server import Server

server_resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'logging': fields.Boolean
}

server_update_args = reqparse.RequestParser()
server_update_args.add_argument('name', type=str)
server_update_args.add_argument('logging', type=bool)

server_post_args = reqparse.RequestParser()
server_post_args.add_argument('name', type=str, required=True)
server_post_args.add_argument('logging', type=bool, required=True)


class ServerEndpoint(Resource):
	@marshal_with(server_resource_fields)
	def patch(self, server_id):
		args = server_update_args.parse_args()
		result = Server.query.filter_by(id=server_id).first()
		if not result:
			abort(404, message="Server with this id does not exist.")
		if args['name']:
			result.name = args['name']
		else:
			abort(406, message="You have to provide name.")
		db.session.commit()
		return result, 200

	def delete(self, server_id):
		result = Server.query.filter_by(id=server_id).first()
		if not result:
			abort(404, message="Server with this id does not exist.")
		db.session.delete(result)
		db.session.commit()
		return "", 200


class ServersEndpoint(Resource):
	@marshal_with(server_resource_fields)
	def get(self):
		result = Server.query.all()
		return result, 200

	def post(self):
		args = server_post_args.parse_args()
		server = Server(name=args['name'], logging=args['logging'])
		db.session.add(server)
		db.session.commit()
		return "", 201


api.add_resource(ServersEndpoint, "/servers")
api.add_resource(ServerEndpoint, "/servers/<int:server_id>")