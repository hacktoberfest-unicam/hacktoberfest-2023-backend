from app import db
from models import GenericModel


class Problem(db.Model, GenericModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(), nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, name, description, difficulty, points):
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.points = points

    def __repr__(self):
        return '<Problem %r>' % self.name
