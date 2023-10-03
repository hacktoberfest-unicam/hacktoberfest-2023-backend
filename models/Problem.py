from app import db
from models import GenericModel


class Problem(db.Model, GenericModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(), nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)

    def __init__(self, name, description, difficulty):
        self.name = name
        self.description = description
        self.difficulty = difficulty

    def __repr__(self):
        return '<Problem %r>' % self.name
