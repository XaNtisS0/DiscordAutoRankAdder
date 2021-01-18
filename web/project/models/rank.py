from ..app import db


class Rank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'Rank(name = {Rank.name}'
