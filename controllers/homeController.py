#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import *


class UserCreator(Resource):
    # Ruta para crear un nuevo usuario
    def post(self):
        user = request.get_json()
        requiredFields = ['firstName', 'lastName',
                          'username', 'email', 'password', 'status']
        if all(fields in requiredFields for fields in user):
            user['password'] = generate_password_hash(
                user['password']).decode('utf8')
            connection.database.users.insert_one(user)
            return {
                'message': 'Bienvenido a Pachaqtec. Cuenta creada con éxito.',
                'success': 'true'}, 200
        else:
            return {
                'message': 'Error en los campos enviados.',
                'success': 'false'}, 200


class LoginController(Resource):

    # Ruta para la API de validar la contraseña con Json Token
    def post(self):
        user = request.get_json()
        requiredFields = ['email', 'password']
        if all(fields in requiredFields for fields in user):
            foundUser = connection.database.users.find_one(
                {'email': user['email']})
            if check_password_hash(foundUser["password"], user['password']):
                expires = datetime.timedelta(days=7)
                access_token = create_access_token(
                    identity=str(1), expires_delta=expires)
                print(foundUser)
                return {
                    'username': foundUser['username'],
                    'token': access_token
                }, 200
            else:
                return {
                    'message': 'Email o contrasena incorrectas',
                    'success': 'false'}, 200
        else:
            return {
                'message': 'Email o contrasena incorrectas',
                'success': 'false'}, 200
