#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Obtenemos configuracion del archivo __init__.py
from . import *


class UserProfileData(Resource):

    # Ruta para la API para editar perfil
    def put(self, username):

        # Capturamos la peticion
        data = request.get_json()

        validFields = ['profile', 'program', 'phone',
                       'email', 'campus']
        updatedFields = []
        cambiadosStr = ": "

        for k, v in data.items():
            updatedFields.append(cambiadosStr.join([k, v]))
            updateMessage = ' - '.join(map(str, updatedFields))

        if any(fields in validFields for fields in data):

            # Creamos el query para el nuevo status
            newValue = {"$set": data}
            # Obtenemos el usuario a modificar
            current_user = connection.mostrarRegistro(username)
            # Actualizamos
            connection.database.users.update_one(current_user, newValue)

            return {
                'message': f"Datos actualizados: {updateMessage}",
                "success": "true"}, 200
        else:
            return {
                'message': 'Ingrese términos válidos',
                'success': 'false'}, 400
