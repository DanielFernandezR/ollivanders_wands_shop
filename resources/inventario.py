from flask_restful import Resource, Api
from config import tienda
from services.service import Service


class Inventario(Resource):

    def get(self):
        return Service.getInventario(tienda)

    def post(self):
        pass