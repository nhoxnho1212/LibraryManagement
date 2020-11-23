from flask import current_app as app
from flask_restful import Api

from server.config import Config
from ..controler.user_controler import User_controler


api = Api(app)

api.add_resource(User_controler, Config.ROUTE['USER'])


