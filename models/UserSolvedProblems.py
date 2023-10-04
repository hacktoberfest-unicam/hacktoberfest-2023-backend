from app import db
from models import GenericModel, Problem, User


class UserSolvedProblems(db.Model, GenericModel):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey(Problem.id), nullable=False)
    bonus_points = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, problem_id, bonus_points):
        self.user_id = user_id
        self.problem_id = problem_id
        self.bonus_points = bonus_points

    def __repr__(self):
        return '<User>' + self.user_id + '<Problem>' + self.problem_id + '<Bonus Points>' + self.bonus_points
