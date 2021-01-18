from ..app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.Integer, db.ForeignKey(
        'server.id'), nullable=False)
    username = db.Column(db.String(32), nullable=False)
    ranks = db.relationship('Rank', backref=db.backref('user'), lazy=True)

    def __repr__(self):
        return f'User(server ID = {User.server_id} name = {User.username}, ranks = {User.ranks}'
