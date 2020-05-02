#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Obtenemos configuracion del archivo __init__.py
from . import *


class UserProfileData(Resource):

    # Ruta para la API para editar perfil
    def put(self, username):

        # Capturamos la peticion
        data = request.get_json()
        # Convertimos a string el contenido recibido
        updatedFields = dicttostr.dictToStr(data)

        # Validamos contenido con opciones válidas
        validFields = config['USER_DATA_OPTIONS']
        if any(fields in validFields for fields in data):

            # Creamos el query para el nuevo status
            newValue = {"$set": data}
            # Obtenemos el usuario a modificar
            current_user = connection.showItem(username)
            # Actualizamos la data del usuario
            connection.updateItem(current_user, newValue)

            return {
                'message': f"Datos actualizados: {updatedFields}",
                "success": "true"}, 200

        # Si los datos no son correctos enviará mensaje
        else:
            return {
                'message': 'Ingrese términos válidos',
                'success': 'false'}, 400
