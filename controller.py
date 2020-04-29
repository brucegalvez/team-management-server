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
        return 'Bienvenido nuevo usuario'


class LoginController(Resource):

    # Ruta para la API de validar la contraseña con Json Token
    def post(self):
        return 'Contraseña verificada. Bienvenido'


class UserStatus(Resource):
    # Ruta para cambiar tu estado de conexion
    def put(self):
        return 'Tu nuevo estado de conexion es: '


class UserProfileData(Resource):
    # Ruta para la API para editar perfil
    def put(self):
        return 'Cambio de informacion exitoso'


class UsersDashboard(Resource):

    # Ruta para la API para listar a los usuarios
    def get(self):
        return 'Estos son todos los usuarios'


class UserInfo(Resource):
    # Ruta para obtener los datos de un solo usuario
    def get(self, id):
        return f'Este es la ruta a para ver los datos del usuario {id}'
