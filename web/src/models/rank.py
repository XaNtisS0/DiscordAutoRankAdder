from marshmallow import fields, Schema
from . import db


class Rank(db.Model):
    __tablename__ = 'ranks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)

    def __init__(self, data):
        self.user_id = data.get('user_id')
        self.name = data.get('name')

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
    def get_all_ranks():
        return Rank.query.all()
  
    @staticmethod
    def get_one_rank(id):
        return Rank.query.get(id)

    def __repr__(self):
        return f'Server(id = {self.id})'