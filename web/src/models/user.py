from . import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.Integer, db.ForeignKey('server.id'), nullable=False)
    username = db.Column(db.String(32), nullable=False)
    ranks = db.relationship('Rank', backref='user', lazy=True)

    def __init__(self, data):
        self.server_id = data.get("server_id")
        self.username = data.get("username")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_servers():
        return User.query.all()
    
    @staticmethod
    def get_one_server(id):
        return User.query.get(id)

    def __repr__(self):
        return f'Server(id = {self.id})'