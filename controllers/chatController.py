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

        # Declaramos la lista de valores posibles
        status_list = ["Conectado", "Ocupado",
                       "Ausente", "No Disponible", "Desconectado"]

        # Capturamos la peticion
        data = request.get_json()
        # Capturamos el nuevo status
        new_status = data["status"]
        # Obtenemos el usuario a modificar
        current_user = connection.showItem("username", username)

        # Validamos que identidad coincida con usuario
        # a modificar data.
        if logged_user != current_user['username']:
            return {
                'message': 'No es el usuario',
                'success': 'false'
            }, 400

        else:
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

                        return {
                            'status': new_status,
                            'Última conexión': f'Última conexión: {lastConnection}',
                            "success": "true"}, 200

                    # De Desconectado a Conectado
                    else:
                        newQuery = {"$set": {
                            "lastConnection": "Ahora",
                            "status": new_status}}

                        # Actualizamos lastConnection
                        connection.updateItem(
                            current_user, newQuery)

                        return {
                            'status': new_status,
                            'Última conexión': 'Ahora',
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

                        return {
                            'status': new_status,
                            'Última conexión': f'Última conexión: {lastTime}',
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

                        return {
                            'status': new_status,
                            'Última conexión': 'Ahora',
                            "success": "true"
                        }, 200
