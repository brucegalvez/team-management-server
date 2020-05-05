#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos propios
from . import *


class UsersDashboard(Resource):
    # Ruta para la API para listar a los usuarios
    def get(self):
        return f'Este es la ruta a para listar a los usuarios', 200


class UserInfo(Resource):
    # Ruta para obtener los datos de un solo usuario
    @jwt_required
    def get(self, username):
        loggedUsername = get_jwt_identity()
        loggedUser = mongo.db.users.find_one({'username': loggedUsername})
        requiredUser = mongo.db.users.find_one({'username': username})
        if not(loggedUser.get('campus') == requiredUser.get('campus') != None):
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
