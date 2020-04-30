#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos propios
from server import *
from logger import *
from utils.connection import Connection
from flask_bcrypt import generate_password_hash, check_password_hash


# Librerias importadas
from flask_restx import Resource
from flask import request

connection = Connection()


class UserCreator(Resource):
    # Ruta para crear un nuevo usuario
    def post(self):
        user = request.get_json()
        requiredFields = ['firstName', 'lastName', 'email', 'password']
        if all(fields in requiredFields for fields in user):
            user['password'] = generate_password_hash(
                user['password']).decode('utf8')
            connection.database.users.insert_one(user)
            return 'Contacto anadido', 201
        else:
            return 'Missing fields', 400


class LoginController(Resource):

    # Ruta para la API de validar la contraseña con Json Token
    def post(self):
        return 'Contraseña verificada. Bienvenido', 201
