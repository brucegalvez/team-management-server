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

        # Capturamos cada key
        new_profile = data.get("profile", "")
        new_program = data.get("program", "")
        new_phone = data.get("phone", "")
        new_email = data.get("email", "")
        new_campus = data.get("campus", "")
        new_profilePic = data.get("profile picture", "")

        # Validamos contenido con opciones válidas
        validFields = config['USER_DATA_OPTIONS']
        if any(fields in validFields for fields in data):
            try:
                if new_phone in data.values():
                    if validate.validateMobile(new_phone) == True:
                        pass
                    else:
                        return {
                            'message': 'Ingrese un número correcto',
                            'success': 'false'}, 400

                if new_email in data.values():
                    if validate.validateEmail(new_email) == True:
                        pass
                    else:
                        return {
                            'message': 'Ingrese un correo válido',
                            'success': 'false'}, 400
            except:
                logging.error('Número y correo inválidos')
                return {
                    'message': 'Datos inválidos',
                    'success': 'false'}, 400
            else:
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
