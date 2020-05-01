#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Obtenemos configuracion del archivo __init__.py
from . import *


class UserProfileData(Resource):
    # Ruta para la API para editar perfil
    def put(self, username):

        # Capturamos la peticion
        data = request.get_json()
        # Capturamos el nuevo status
        new_profile = data["profile"]
        # Creamos el query para el nuevo status
        newValue = {"$set": data}
        # Obtenemos el usuario a modificar
        current_user = connection.mostrarRegistro(username)

        # Validamos que el estado sea un str
        if new_profile is not None and type(new_profile) == str:
            connection.database.users.update_one(current_user, newValue)
            return {
                'profile': new_profile,
                "success": "true"}, 200
        else:
            return {
                'message': 'Ingrese términos válidos',
                'success': 'false'}, 400
