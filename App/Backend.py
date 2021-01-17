from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

db.create_all()


class ServerModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'Server(id = {ServerModel.id}, name = {ServerModel.name})'


server_post_args = reqparse.RequestParser()
server_post_args.add_argument('name', type=str, required=True)

server_update_args = reqparse.RequestParser()
server_update_args.add_argument('name', type=str)


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    server_id = db.Column(db.Integer, db.ForeignKey(
        'ServerModel.id'), nullable=False)
    server = db.relationship(
        'ServerModel', backref=db.backref('users', lazy=True))

    username = db.Column(db.String(32), nullable=False)
    ranks = db.Column(db.List, nullable=False)

    def __repr__(self):
        return f'User(server ID = {UserModel.server_id} name = {UserModel.username}, ranks = {UserModel.ranks}'


user_post_args = reqparse.RequestParser()
user_post_args.add_argument("server_id", type=int,
                            help="ServerId is required.", required=True)
user_post_args.add_argument(
    "username", type=str, help="Name is required.", required=True)
user_post_args.add_argument(
    "ranks", type=list, help="Ranks list is required.", required=True)

user_update_args = reqparse.RequestParser()
user_update_args.add_argument("server_id", type=int)
user_update_args.add_argument("username", type=str)
user_update_args.add_argument("ranks", type=list)

server_resource_fields = {
    'id': fields.Integer,
    'name': fields.String
}

user_resource_fields = {
    'id': fields.Integer,
    'server_id': fields.Integer,
    'server': fields.String,
    'name': fields.String,
    'ranks': fields.List
}


class Server(Resource):
    @ marshal_with(server_resource_fields)
    def get(self):
        result = ServerModel.query.all()
        return result, 200

    def post(self):
        args = server_post_args.parse_args()
        server = ServerModel(name=args['name'])
        db.session.add(server)
        db.session.commit()
        return "", 201
    
api.add_resource(Server, endpoint="/servers")

class ServerWithId(Resource):
    @marshal_with(server_resource_fields)
    def patch(self, server_id):
        args = server_update_args.parse_args()
        result = ServerModel.query.filter_by(id = server_id).first()
        if not result:
            abort(404, message="Server with this id does not exist.")
        if args['name']:
            result.name = args['name']
        else:
            abort(406, message="You have to provide name.")
        db.session.commit()
        return result, 200

    def delete(self, server_id):
        args = server_update_args.parse_args()
        result = ServerModel.query.filter_by(id = server_id).first()
        if not result:
            abort(404, message="Server with this id does not exist.")
        db.session.delete(result)
        return "", 200

api.add_resource(ServerWithId, endpoint="/servers/<int:server_id>")

class Users(Resource):
    @ marshal_with(user_resource_fields)
    def get(self, serv_id):
        result = UserModel.query.filter_by(server_id=serv_id).all()
        return result, 200

    def post(self, serv_id):
        args = user_post_args.parse_args()
        users_in_server = ServerModel.query.filer_by(id=serv_id)
        user = UserModel(username=args['username'], ranks=args['ranks'])
        users_in_server.users.append(user)
        db.session.add(users_in_server)
        db.session.commit()
        return "", 201

api.add_resource(Users, endpoint="/<int:serv_id>/Users")

class UsersWithId(Resource):
    @marshal_with(user_resource_fields)
    def patch(self, serv_id, user_id):
        args = user_update_args.parse_args()
        result = UserModel.query.filter_by(id = user_id, server_id = serv_id).first()
        if not result:
            abort(404, message="User with this id does not exist.")
        for arg in args:
            if arg:
                result.arg = arg

        db.session.commit()
        return result, 200

    def delete(self, serv_id, user_id):
        result = UserModel.query.filter_by(id = user_id, server_id = serv_id)
        if not result:
            abort(404,message="User with this id does not exist.")
        db.session.delete(result)
        return "", 200