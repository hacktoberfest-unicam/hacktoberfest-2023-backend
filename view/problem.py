"""
Flask view that will return a JSON response containing the
problem details.

The problem details are in the following format:
{
    "name": "problem name",
    "description": "problem description",
    "difficulty": "problem difficulty",
}
"""

from flask import request
from flask.views import MethodView

from controller import problem as problem_controler


class ProblemAPI(MethodView):
    def get(self, problem_id=None):
        if problem_id is None:
            problem = problem_controler.get_all_problem()
        else:
            problem = problem_controler.get_problem(problem_id)
        return problem

    def post(self):
        params = request.json
        problem = problem_controler.create_problem(params['name'], params['description'], params['difficulty'])
        return problem

    def put(self, problem_id):
        params = request.json
        problem = problem_controler.update_problem(problem_id, params['name'], params['description'],
                                                   params['difficulty'])
        return problem

    def delete(self, problem_id):
        problem = problem_controler.delete_problem(problem_id)
        return problem
