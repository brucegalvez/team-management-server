#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos propios
from server import *
from logger import *

# Librerias importadas
from flask_restx import Resource


class UserStatus(Resource):
    # Ruta para cambiar tu estado de conexion
    def put(self):
        return 'Tu nuevo estado de conexion es: ', 204


class UserProfileData(Resource):
    # Ruta para la API para editar perfil
    def put(self):
        return 'Cambio de informacion exitoso', 204
