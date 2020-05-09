#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos propios
from . import *


class UserInfo(Resource):
    # Ruta para obtener los datos de un solo usuario
    @jwt_required
    def get(self, username):
        loggedUsername = get_jwt_identity()
        loggedUser = mongo.db.users.find_one({'username': loggedUsername})
        requiredUser = mongo.db.users.find_one({'username': username})
        if requiredUser == None or loggedUser == None:
            return {
                'message': 'No cuenta con los permisos necesarios.',
                'success': 'false'}, 200
        elif not(loggedUser.get('campus') == requiredUser.get('campus')):
            return {
                'message': 'No cuenta con los permisos necesarios.',
                'success': 'false'}, 200
        else:
            del requiredUser['password']
            del requiredUser['_id']
            return {
                'message': 'OK.',
                'content': requiredUser,
                'success': 'true'}, 200


class UsersDashboard(Resource):

    # Ruta para la API para listar a los usuarios
    @jwt_required
    def get(self):

        # Obtenemos la identidad del usuario loggeado
        loggedUsername = get_jwt_identity()

        # Capturamos objeto json de la petición
        data = request.get_json()

        firstName = data.get('firstName')
        program = data.get('program')

        if mongo.db.users.find({'username': loggedUsername}) == None:
            return {
                'message': 'No tiene los permisos necesarios',
                'success': 'false'
            }, 400

        else:
            found = []

            for user in mongo.db.users.find(
                    {"$or":
                     [
                         {"firstName": {'$regex': f'{firstName}'}},
                         {"program": {'$regex': f'{program}'}}
                     ]
                     }):
                del user['password']
                del user['_id']
                del user['lastConnection']
                del user['status']
                found.append(user)
            if found == []:
                return {'message': 'No se encontraron usuarios con esos datos',
                        'success': 'false'}, 200
            else:
                return {'message': 'Usuarios encontrados.',
                        'content': found,
                        'success': 'true'}, 200
