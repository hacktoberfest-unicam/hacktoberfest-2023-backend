import sqlalchemy.exc

from app import db
from models import GenericModel


class GenericController(object):
    def __init__(self, model: type['GenericModel']):
        self.__model = model

    def get_all(self):
        return [model.to_dict() for model in db.session.query(self.__model).all()]

    def get_by_id(self, crud_id: int):
        model = db.session.query(self.__model).filter_by(id=crud_id).first()
        if not model:
            return None
        return model.to_dict()

    def get_by_param(self, param_name: str, param_value: str):
        model = db.session.query(self.__model).filter_by(**{param_name: param_value}).first()
        if not model:
            return None
        return model.to_dict()

    def create(self, **kwargs):
        try:
            model = self.__model(**kwargs)
            db.session.add(model)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return {"error": "Duplicate entry"}
        return model.to_dict()

    def update(self, crud_id: int, **kwargs):
        model = db.session.query(self.__model).filter_by(id=crud_id).first()
        if not model:
            return None
        for key, value in kwargs.items():
            setattr(model, key, value)
        db.session.commit()
        return model.to_dict()

    def delete(self, crud_id: int):
        model = db.session.query(self.__model).filter_by(id=crud_id).first()
        if not model:
            return False
        db.session.delete(model)
        return True
