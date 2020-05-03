#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Obtenemos configuracion del archivo __init__.py
from . import *


class UserProfileData(Resource):

    # Ruta para la API para editar perfil
    @jwt_required
    def put(self, username):

        # Obtenemos la identidad de quien hace la peticion
        logged_user = get_jwt_identity()

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
        validFields = ["profile", "program", "phone",
                       "email", "campus", "profile picture", "tags"]

        # Validamos que identidad coincida con usuario
        # a modificar data.

        if logged_user != username:
            return {
                'message': 'No es el usuario',
                'success': 'false'
            }, 400

        else:
            # Validamos que quiera cambiar datos permitidos
            if not any(fields in validFields for fields in data):
                # Si los datos no son correctos enviará mensaje
                return {
                    'message': 'Ingrese términos válidos',
                    'success': 'false'}, 400
            else:
                try:
                    # Validamos si el telefono es real
                    if new_phone in data.values():
                        if not validate.validateMobile(new_phone):
                            return {
                                'message': 'Ingrese un número correcto',
                                'success': 'false'}, 400
                        else:
                            pass

                    # Validamos si el correo es valido
                    if new_email in data.values():
                        if not validate.validateEmail(new_email):
                            return {
                                'message': 'Ingrese un correo válido',
                                'success': 'false'}, 400
                        else:
                            pass
                except:
                    logging.error('Número y correo inválidos')
                    return {
                        'message': 'Datos inválidos',
                        'success': 'false'}, 400
                else:
                    # Creamos el query para el nuevo status
                    newValue = {"$set": data}
                    # Obtenemos el usuario a modificar
                    current_user = connection.showItem("username", username)
                    # Actualizamos la data del usuario
                    connection.updateItem(current_user, newValue)

                    return {
                        'message': f"Datos actualizados: {updatedFields}",
                        "success": "true"}, 200
