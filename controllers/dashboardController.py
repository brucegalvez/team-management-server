#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos propios
from . import *


class UsersDashboard(Resource):

    # Ruta para la API para listar a los usuarios
    def get(self):
        return 'Estos son los estudiantes de tu especialidad.'


class UserInfo(Resource):
    # Ruta para obtener los datos de un solo usuario
    def get(self, id):
        return f'Este es la ruta a para ver los datos del usuario {id}', 200
