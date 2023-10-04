from typing import Union

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)


from models import GenericModel, Problem, User, UserSolvedProblems


def add_rules(local_app, base_url, problem_list: list[str], base_api_name: str, model: type['GenericModel'], param_name: Union[str, list[str]]):
    local_app.add_url_rule(f'/{base_url}/<int:crud_id>',
                           view_func=GenericCRUD.as_view(base_api_name, model, problem_list, param_name),
                           methods=['GET', 'PUT', 'DELETE'])
    local_app.add_url_rule(f'/{base_url}',
                           view_func=GenericCRUD.as_view(f'{base_api_name}_part_2', model, problem_list, param_name),
                           methods=['GET', 'POST'])


with app.app_context():
    db.create_all()

from view import HelloAPI, GenericCRUD

app.add_url_rule('/', view_func=HelloAPI.as_view('hello'), methods=['GET'])
add_rules(app, 'problem', ['name', 'description', 'difficulty', 'points'], 'problem_api', Problem, 'name')
add_rules(app, 'user', ['github_username', 'github_profile_picture', 'github_url'], 'user_api', User, 'github_username')
add_rules(app, 'solved', ['user_id', 'problem_id', 'bonus_points'], 'user_solved_problems_api', UserSolvedProblems, ['user_id', 'problem_id'])
