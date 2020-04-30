#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos propios
from server import *
from logger import *

# Librerias importadas
from flask_restx import Resource


class UsersDashboard(Resource):

    # Ruta para la API para listar a los usuarios
    def get(self):
        return 'Estos son todos los usuarios', 200


class UserInfo(Resource):
    # Ruta para obtener los datos de un solo usuario
    def get(self, id):
        return f'Este es la ruta a para ver los datos del usuario {id}', 200
