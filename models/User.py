from app import db
from models import GenericModel


class User(db.Model, GenericModel):
    id = db.Column(db.Integer, primary_key=True)
    github_username = db.Column(db.String(80), unique=True, nullable=False)
    github_profile_picture = db.Column(db.String(), nullable=False)
    github_url = db.Column(db.String(), nullable=False)

    def __init__(self, github_username, github_profile_picture, github_url):
        self.github_username = github_username
        self.github_profile_picture = github_profile_picture
        self.github_url = github_url

    def __repr__(self):
        return '<User %r>' % self.github_username
