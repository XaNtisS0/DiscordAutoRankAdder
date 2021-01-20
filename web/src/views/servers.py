from flask_restful import Resource, reqparse, abort, fields, marshal_with

from ..run import db, api

from ..models.server import Server

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


server_delete_args = reqparse.RequestParser()
server_delete_args.add_argument('name', type=str)

server_get_args = reqparse.RequestParser()
server_get_args.add_argument('name', type=str)


class ServersEndpoint(Resource):
    @marshal_with(server_resource_fields)
    def get(self):
        args = server_get_args.parse_args()
        if args['name']:
            result = Server.query.filter_by(name=args['name']).all()
            return result, 200
        if not args:
            result = Server.query.all()
            return result, 200

    def post(self):
        args = server_post_args.parse_args()
        server = Server(name=args['name'], logging=args['logging'])
        db.session.add(server)
        db.session.commit()
        return "", 201


class ServerEndpoint(Resource):
    @marshal_with(server_resource_fields)
    def patch(self, server_id):
        args = server_update_args.parse_args()
        result = Server.query.filter_by(id=server_id).first()
        if not result:
            abort(404, message="Server with this id does not exist.")
        if args['name']:
            result.name = args['name']
        if args['logging']:
            result.logging = args['logging']
        db.session.commit()
        return result, 200

    def delete(self, server_id):
        args = server_delete_args.parse_args()
        result = {}
        if args['name']:
            result = Server.query.filter_by(name=args['name']).delete()
            if not result:
                abort(404, message="Server with this name does not exist.")
        elif not args:
            result = Server.query.filter_by(id=server_id).first().delete()
            if not result:
                abort(404, message="Server with this id does not exist.")
        db.session.commit()
        return "", 200


api.add_resource(ServersEndpoint, "/servers")
api.add_resource(ServerEndpoint, "/servers/<int:server_id>")
