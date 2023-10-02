"""
Problem controller.

This module is used as interface between the view and the model, performs all the operations in order to enforce the MVC pattern.
"""
from models import Problem
from app import db

def get_problem(problem_id):
    """
    Get a problem by id.

    :param problem_id: the problem id
    :return: the problem
    """
    problem = db.session.query(Problem).filter_by(id=problem_id).first()
    if not problem:
        return None
    return problem.to_dict()


def create_problem(name, description, difficulty):
    """
    Create a new problem.

    :param name: the problem name
    :param description: the problem description
    :param difficulty: the problem difficulty
    :return: the problem
    """
    problem = Problem(name=name, description=description, difficulty=difficulty)
    db.session.add(problem)
    db.session.commit()
    return problem.to_dict()


def update_problem(problem_id, name, description, difficulty):
    """
    Update a problem.

    :param problem_id: the problem id
    :param name: the problem name
    :param description: the problem description
    :param difficulty: the problem difficulty
    :return: the problem
    """
    problem = db.session.query(Problem).filter_by(id=problem_id).first()
    if not problem:
        return None
    problem.name = name
    problem.description = description
    problem.difficulty = difficulty
    db.session.commit()
    return problem.to_dict()


def delete_problem(problem_id):
    """
    Delete a problem.

    :param problem_id: the problem id
    :return: True if the problem has been deleted, False otherwise
    """
    problem = db.session.query(Problem).filter_by(id=problem_id).first()
    if not problem:
        return False
    db.session.delete(problem)
    return True


def get_all_problem():
    """
    Get all the problems.

    :return: the problems
    """
    problems = db.session.query(Problem).all()
    return [problem.to_dict() for problem in problems]
