from . import db


class Server(db.Model):
    __tablename__ = 'servers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    logging = db.Column(db.Boolean, nullable=False)
    users = db.relationship('User', backref='server', lazy=True)
    
    def __init__(self, data):
        self.name = data.get("name")
        self.logging = data.get("logging")

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
        return Server.query.all()
    
    @staticmethod
    def get_one_server(id):
        return Server.query.get(id)

    def __repr__(self):
        return f'Server(id = {self.id})'