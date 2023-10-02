"""
Defines the SQLAlchemy ORM representation for a Problem.
A problem is identified by its unique id, and has a name, a description and a difficulty.
"""
from app import db


class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(), nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Problem %r>' % self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'difficulty': self.difficulty,
        }
