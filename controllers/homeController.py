#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import *


class UserCreator(Resource):
    # Ruta para crear un nuevo usuario
    def post(self):
        user = request.get_json()
        requiredFields = ['firstName', 'lastName',
                          'username', 'email', 'password']
        if list(user.keys()) != requiredFields:
            return {
                'message': 'Error en los campos enviados.',
                'success': 'false'}, 200
        elif not (
            validate.validateGivenName(user['firstName']) and
            validate.validateGivenName(user['lastName']) and
            validate.validateUsername(user['username']) and
            validate.validateEmail(user['email']) and
            validate.validatePassword(user['password'])
        ):
            return {
                'message': 'Error en los campos enviados.',
                'success': 'false'}, 200
        elif list(mongo.db.users.find(
                {"$or": [{'email': user['email']}, {'username': user['username']}]})):
            return {
                'message': 'Existe un usuario con el mismo email o username.',
                'success': 'false'}, 200
        else:
            user['password'] = generate_password_hash(
                user['password']).decode('utf8')
            user['status'] = 'Conectado'
            user['lastConnected'] = 'Ahora'
            mongo.db.users.insert_one(user)
            return {
                'message': 'Cuenta creada con éxito.',
                'success': 'true'}, 200


class LoginController(Resource):
    # Ruta para la API de validar la contraseña con Json Token
    def post(self):
        user = request.get_json()
        requiredFields = ['email', 'password']
        if list(user.keys()) != requiredFields:
            return {
                'message': 'Email o contraseña incorrectas',
                'success': 'false'}, 200
        elif not (
                validate.validateEmail(user['email']) and
                validate.validatePassword(user['password'])):
            return {
                'message': 'Email o contraseña incorrectas',
                'success': 'false'}, 200
        else:
            foundUser = mongo.db.users.find_one({'email': user['email']})
            if not (
                    foundUser and
                    check_password_hash(foundUser["password"], user['password'])):
                return {
                    'message': 'Email o contraseña incorrectas',
                    'success': 'false'}, 200
            else:
                expires = datetime.timedelta(days=7)
                access_token = create_access_token(
                    identity=foundUser['username'], expires_delta=expires)
                return {
                    'message': 'Login con exito.',
                    'success': 'true',
                    'content': {
                        'username': foundUser['username'],
                        'token': access_token
                    }}, 200
