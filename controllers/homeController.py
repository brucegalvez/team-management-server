#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos propios
from server import *
from logger import *

# Librerias importadas
from flask_restx import Resource


class UserCreator(Resource):
    # Ruta para crear un nuevo usuario
    def post(self):
        return 'Bienvenido nuevo usuario', 201


class LoginController(Resource):

    # Ruta para la API de validar la contraseña con Json Token
    def post(self):
        return 'Contraseña verificada. Bienvenido', 201
