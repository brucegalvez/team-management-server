#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Obtenemos configuracion del archivo __init__.py
from . import *


class UserStatus(Resource):
    # Ruta para cambiar tu estado de conexion
    @jwt_required
    def put(self, username):

        # Obtenemos la identidad de quien hace la peticion
        logged_user = get_jwt_identity()

        # Capturamos la peticion
        data = request.get_json()
        # Capturamos el nuevo status
        new_status = data["status"]
        # Obtenemos el usuario a modificar
        current_user = connection.showItem("username", username)

        # Validamos que la opcion este dentro de lo permitido
        if not new_status in status_list:
            return {
                'message': 'Elija una opción correcta',
                'success': 'false'}, 400

        # Procede la solicitud
        else:
            if current_user['status'] != 'Conectado':
                # De Otro a Otro
                if new_status != 'Conectado':
                    # Si el status a actualizar no era Conectado,
                    # Obtenemos ultima conexion de usuario
                    lastConnection = current_user['lastConnection']
                    newQuery = {"$set": {
                        "lastConnection": lastConnection,
                        "status": new_status}}

                    # Actualizamos lastConnection
                    connection.updateItem(
                        current_user, newQuery)

                    return {'message': 'Obteniendo status y última conexión',
                            'content': {
                                'status': new_status,
                                'lastConnection': lastConnection},
                            "success": "true"}, 200

                # De Desconectado a Conectado
                else:
                    newQuery = {"$set": {
                        "lastConnection": "Ahora",
                        "status": new_status}}

                    # Actualizamos lastConnection
                    connection.updateItem(
                        current_user, newQuery)

                    return {'message': 'Obteniendo status y última conexión',
                            'content': {'status': new_status,
                                        'lastConnection': 'Ahora'},
                            "success": "true"
                            }, 200

            else:
                # De Otro a Desconectado"
                if new_status != 'Conectado':
                    # Creamos query
                    lastTime = getTime.getTime()
                    newQuery = {"$set": {
                        "lastConnection": lastTime,
                        "status": new_status}}

                    # Actualizamos status y lastConnection
                    connection.updateItem(
                        current_user, newQuery)

                    return {'message': 'Obteniendo status y última conexión',
                            'content': {'status': new_status,
                                        'lastConnection': lastTime},
                            "success": "true"}, 200
                # De Conectado a Conectado
                else:
                    # Creamos query
                    newQuery = {"$set": {
                        "lastConnection": "Ahora",
                        "status": new_status}}

                    # Actualizamos status y lastConnection
                    connection.updateItem(
                        current_user, newQuery)

                    return {'message': 'Obteniendo status y última conexión',
                            'content': {'status': new_status,
                                        'lastConnection': 'Ahora'},
                            "success": "true"
                            }, 200


class ChatDisplay(Resource):
    # Ruta para la API para listar a los usuarios conectados y desconectados

    @jwt_required
    def get(self):
        connected = []
        disconnected = []
        ocupied = []
        absent = []
        unavailable = []
        data = request.get_json()
        username = data['username']
        user_program = data['program']

        if not list(connection.showList('username', username)):

            return {'message': 'Usuario no existe',
                    'success': 'false'}, 400

        else:

            # Obtenemos la lista de conectados
            for user in connection.showList("status", "Conectado"):
                username = user['username']
                firstName = user['firstName']
                lastName = user['lastName']
                lastConnection = user['lastConnection']
                status = user['status']
                program = user['program']
                if user_program == program:
                    connected.append(
                        {'firstName': f'{firstName}', 'lastName': f'{lastName}',
                         'username': f'{username}', 'status': f'{status}',
                         'lastConnection': f'{lastConnection}'})

            # Obtenemos la lista de desconectados
            for user in connection.showList("status", "Desconectado"):
                username = user['username']
                firstName = user['firstName']
                lastName = user['lastName']
                lastConnection = user['lastConnection']
                program = user['program']
                if user_program == program:
                    disconnected.append(
                        {'firstName': f'{firstName}', 'lastName': f'{lastName}',
                         'username': f'{username}', 'status': f'{status}',
                         'lastConnection': f'{lastConnection}'})

            # Obtenemos la lista de ocupados
            for user in connection.showList("status", "Ocupado"):
                username = user['username']
                firstName = user['firstName']
                lastName = user['lastName']
                lastConnection = user['lastConnection']
                program = user['program']
                if user_program == program:
                    disconnected.append(
                        {'firstName': f'{firstName}', 'lastName': f'{lastName}',
                         'username': f'{username}', 'status': f'{status}',
                         'lastConnection': f'{lastConnection}'})

            # Obtenemos la lista de No Disponibles
            for user in connection.showList("status", "No Disponible"):
                username = user['username']
                firstName = user['firstName']
                lastName = user['lastName']
                lastConnection = user['lastConnection']
                program = user['program']
                if user_program == program:
                    disconnected.append(
                        {'firstName': f'{firstName}', 'lastName': f'{lastName}',
                         'username': f'{username}', 'status': f'{status}',
                         'lastConnection': f'{lastConnection}'})

            # Obtenemos la lista de Ausentes
            for user in connection.showList("status", "Ausente"):
                username = user['username']
                firstName = user['firstName']
                lastName = user['lastName']
                lastConnection = user['lastConnection']
                program = user['program']
                if user_program == program:
                    disconnected.append(
                        {'firstName': f'{firstName}', 'lastName': f'{lastName}',
                         'username': f'{username}', 'status': f'{status}',
                         'lastConnection': f'{lastConnection}'})

            return {'message': f'Obteniendo listas por status de {user_program}',
                    'content': {'Conectado': connected,
                                'Desconectado': disconnected,
                                'Ocupado': ocupied,
                                'Ausente': absent,
                                'No Disponible': unavailable
                                },
                    'success': 'true'
                    }
