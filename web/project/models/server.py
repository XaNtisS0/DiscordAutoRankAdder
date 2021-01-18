from ..app import db


class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    logging = db.Column(db.Boolean, nullable=False)
    users = db.relationship(
        'User', backref=db.backref('server', lazy=True))

    def __repr__(self):
        return f'Server(id = {Server.id}, name = {Server.name})'
