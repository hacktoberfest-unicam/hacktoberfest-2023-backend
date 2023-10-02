from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)


def add_rules(local_app):
    from view import HelloAPI, ProblemAPI
    local_app.add_url_rule('/', view_func=HelloAPI.as_view('hello'), methods=['GET'])
    local_app.add_url_rule('/problem/<int:problem_id>', view_func=ProblemAPI.as_view('problem_api'),
                           methods=['GET', 'PUT', 'DELETE'])
    local_app.add_url_rule('/problem', view_func=ProblemAPI.as_view('problem_api_update'), methods=['POST', 'PUT'])


add_rules(app)

with app.app_context():
    db.create_all()
