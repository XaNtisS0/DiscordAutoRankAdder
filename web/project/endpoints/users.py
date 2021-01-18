from flask_restful import Resource, reqparse, abort, fields, marshal_with

from ..app import db, api
from ..models.rank import Rank
from ..models.server import Server

from ..models.user import User

user_post_args = reqparse.RequestParser()
user_post_args.add_argument(
    "username",
    type=str,
    help="Name is required.",
    required=True)
user_post_args.add_argument(
    "ranks",
    type=list,
    location='json',
    help="Ranks list is required.",
    required=True)

user_update_args = reqparse.RequestParser()
user_update_args.add_argument("server_id", type=int)
user_update_args.add_argument("username", type=str)
user_update_args.add_argument("ranks", type=list, location='json')


class UsersEndpoint(Resource):
    def get(self, serv_id):
        users = User.query.filter_by(server_id=serv_id).all()

        if not users:
            abort(404, message="No users with this server id.")

        response = []
        for user in users:
            user_id = user.id
            ranks = Rank.query.filter_by(user_id=user_id).all()
            ranks_array = [rank.name for rank in ranks]
            response.append({
                "id": user.id,
                "server_id": user.server_id,
                "username": user.username,
                "ranks": ranks_array
            })

        return response, 200

    def post(self, serv_id):
        args = user_post_args.parse_args()

        server = Server.query.get(serv_id)
        user = User(server=server, username=args['username'])

        db.session.add(user)
        db.session.commit()

        for rank in args['ranks']:
            item = Rank(name=rank, user=user)
            db.session.add(item)

        db.session.commit()
        return "", 201


class UserEndpoint(Resource):
    def patch(self, serv_id, user_id):
        args = user_update_args.parse_args()

        user = User.query.filter_by(id=user_id).first()

        if not user:
            abort(404, message="User with this id does not exist on this server.")

        if args['username']:
            user.username = args['username']
        if args['ranks']:
            ranks = Rank.query.filter_by(user_id=user_id).all()
            ranks_array = [rank.name for rank in ranks]
            if set(args['ranks']) != set(ranks_array):
                db.session.delete(ranks)
                for rank in args['ranks']:
                    item = Rank(name=rank, user=user)
                    db.session.add(item)
        if args['server_id']:
            user.server_id = args['server_id']

        db.session.commit()

        user = User.query.filter_by(id=user_id).first()

        ranks = Rank.query.filter_by(user_id=user_id).all()
        ranks_array = [rank.name for rank in ranks]

        response = {
            "id": user.id,
            "server_id": user.server_id,
            "username": user.username,
            "ranks": ranks_array
        }

        return response, 200

    def delete(self, serv_id, user_id):
        result = User.query.filter_by(id=user_id).filter_by(server_id=serv_id).first()
        Rank.query.filter_by(user_id=user_id).delete()

        if not result:
            abort(404, message="User with this id does not exist.")

        db.session.delete(result)
        db.session.commit()
        return "", 200


api.add_resource(UsersEndpoint, "/<int:serv_id>/users")
api.add_resource(UserEndpoint, "/<int:serv_id>/users/<int:user_id>")
