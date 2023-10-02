"""
Hello view, just for testing has a get on '/', returns the time
"""
from datetime import datetime

from flask.views import MethodView

from flask import jsonify


class HelloAPI(MethodView):
    def get(self):
        return jsonify({'hello': 'world', 'time': str(datetime.now())})
