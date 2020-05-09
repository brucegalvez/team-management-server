#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos propios
from . import *
import json


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
        # Validamos que sea un usuario de la base de datos
        if mongo.db.users.find({'username': loggedUsername}) == None:
            return {
                'message': 'No tiene los permisos necesarios',
                'success': 'false'
            }, 400

        else:
            # Capturamos objeto json de la petición
            data = request.get_json()
            # Creamos una lista vacía para almacenar la data a recoger
            found = []
            # Validamos si el body de la petición está vacía
            if data == None:
                for user in mongo.db.users.find():
                    del user['password']
                    del user['_id']
                    del user['lastConnection']
                    del user['status']
                    found.append(user)

                return {'message': 'Usuarios encontrados.',
                        'content': found,
                        'success': 'true'}, 200

            # Si la petición tiene contenido, procedemos a procesar la información
            else:

                text = data.get('text')
                program = data.get('program')
                order = data.get('order')
                try:
                    # Si el usuario pide mediante texto o programa de
                    # especializaciòn, mostramos las coincidencias
                    if "program" in data.keys() and "text" in data.keys():
                        namesList = text.split()
                        for name in namesList:
                            for user in mongo.db.users.find(
                                    {"$or": [
                                        {"$and": [{"firstName": {'$regex': f'{name}'}}, {
                                            "program": {'$regex': f'{program}'}}]},
                                        {"$and": [{"lastName": {'$regex': f'{name}'}}, {
                                            "program": {'$regex': f'{program}'}}]}
                                    ]}):

                                del user['password']
                                del user['_id']
                                del user['lastConnection']
                                del user['status']
                                found.append(user)

                    # Si no hay texto, pero sí programa. Mostramos los usuarios correspondientes.
                    if "text" not in data.keys() and "program" in data.keys():
                        for user in mongo.db.users.find(
                                {"$or": [
                                    {"program": {'$regex': f'{program}'}}
                                ]}):

                            del user['password']
                            del user['_id']
                            del user['lastConnection']
                            del user['status']
                            found.append(user)
                    # Si hay texto, pero no programa. Mostramos los usuarios que coincidan
                    # con las palabras ingresadas.
                    if "text" in data.keys() and "program" not in data.keys():
                        namesList = text.split()
                        for name in namesList:
                            for user in mongo.db.users.find(
                                    {"$or": [
                                        {"firstName": {'$regex': f'{name}'}},
                                        {"lastName": {'$regex': f'{name}'}}
                                    ]}):

                                del user['password']
                                del user['_id']
                                del user['lastConnection']
                                del user['status']
                                found.append(user)

                    # Si hay orden en la petición, pero no otros valores,
                    # armamos la lista con todos los valores.
                    if ("order" in data.keys() and
                        "program" not in data.keys() and
                            "text" not in data.keys()):
                        for user in mongo.db.users.find():

                            del user['password']
                            del user['_id']
                            del user['lastConnection']
                            del user['status']
                            found.append(user)

                finally:
                    # Si no hay coincidencias, no devuelve nada
                    if found == []:
                        return {'message': 'No se encontraron usuarios con esos datos',
                                'success': 'false'}, 400
                    else:
                        # Validamos si el orden pedido es válido
                        if "order" in data.keys():
                            if not order.upper() in ['A-Z', 'Z-A']:
                                return {'message': 'No es un orden válido',
                                        'success': 'false'}, 400
                            else:
                                # Ordenamos los datos de forma ascendente
                                # o descendente según correponda
                                if order.upper() == 'A-Z':
                                    sortedFound = sorted(
                                        found, key=lambda i: i['firstName'], reverse=False)
                                if order.upper() == 'Z-A':
                                    sortedFound = sorted(
                                        found, key=lambda i: i['firstName'], reverse=True)

                                return {'message': 'Usuarios encontrados.',
                                        'content': sortedFound,
                                        'success': 'true'}, 200
                        # Devolvemos el contenido de la lista
                        else:
                            return {'message': 'Usuarios encontrados.',
                                    'content': found,
                                    'success': 'true'}, 200
