from flask import request
from flask.views import MethodView

from app import db
from controller import GenericController


class GenericCRUD(MethodView):
    init_every_request = False

    def __init__(self, model: db.Model, params_list: list[str], param_name: str, controller: GenericController = None):
        if controller is None:
            controller = GenericController(model)
        self.__model = model
        self.__controller = controller
        self.__params_list = params_list
        self.__param_name = param_name

    def get(self, crud_id: int = None):
        result = None
        if crud_id is None:
            result = self.__controller.get_all()
        elif crud_id is not None:
            result = self.__controller.get_by_id(crud_id)
        elif self.__param_name is list and len(self.__param_name) > 0 and all(param in request.args for param in self.__param_name):
            result = self.__controller.get_by_params(self.__param_name, [request.args[param] for param in self.__param_name])
        elif self.__param_name in request.args:
            result = self.__controller.get_by_param(self.__param_name, request.args[self.__param_name])
        if result is None:
            return {"error": "Not found"}, 404
        return result

    def post(self):
        params = request.json
        params_dict = {param_name: params[param_name] for param_name in self.__params_list}
        problem = self.__controller.create(**params_dict)
        return problem

    def put(self, crud_id):
        params = request.json
        params_dict = {param_name: params[param_name] for param_name in self.__params_list}
        problem = self.__controller.update(crud_id, **params_dict)
        return problem

    def delete(self, crud_id):
        problem = self.__controller.delete(crud_id)
        return problem
