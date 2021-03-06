#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Obtenemos configuracion del archivo __init__.py
from . import *


class UserProfileData(Resource):

    # Ruta para la API para editar perfil
    @jwt_required
    def put(self, username):

        # Obtenemos la identidad de quien hace la peticion
        loggedUsername = get_jwt_identity()

        # Capturamos la peticion
        data = request.get_json()

        # Capturamos cada key
        new_profile = data.get("profile", "")
        new_program = data.get("program", "")
        new_phone = data.get("phone", "")
        new_email = data.get("email", "")
        new_campus = data.get("campus", "")
        new_program = data.get("program", "")
        new_profilePic = data.get("profile picture", "")

        current_user = mongo.db.users.find_one({'username': username})

        if not(loggedUsername == current_user.get('username') != None):
            return {
                'message': 'No cuenta con los permisos necesarios.',
                'success': 'false'}, 400
        else:
            # Validamos que quiera cambiar datos permitidos
            if not any(fields in validFields for fields in data):
                # Si los datos no son correctos enviará mensaje
                return {
                    'message': 'Ingrese términos válidos',
                    'success': 'false'}, 400
            else:
                try:
                    # Validamos que el perfil no tenga más de 150 caracteres
                    if new_profile in data.values():
                        if not validate.validateProfile(new_profile):
                            return {'message': 'Tiene más de 150 caracteres',
                                    'success': 'false'}, 400
                        else:
                            pass
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

                    # Validamos si la nueva sede existe
                    if new_campus in data.values():
                        if not new_campus in validCampus:
                            return {
                                'message': 'No es una sede existente',
                                'success': 'false'}, 400
                        else:
                            pass
                    # Validamos si el nuevo prograama existe
                    if new_program in data.values():
                        if not new_program in validPrograms:
                            return {
                                'message': 'No es un programa válido',
                                'success': 'false'
                            }, 400
                        else:
                            pass

                except:
                    logging.error('Tiene datos inválidos')
                    return {
                        'message': 'Datos inválidos',
                        'success': 'false'}, 400
                else:
                    # Creamos el query para el nuevo status
                    newValue = {"$set": data}
                    # Obtenemos el usuario a modificar
                    current_user = mongo.db.users.find_one(
                        {"username": username})
                    # Actualizamos la data del usuario
                    mongo.db.users.update_one(current_user, newValue)

                    return {
                        'message': "Datos actualizados",
                        'content': data,
                        "success": "true"}, 200


class UserTags(Resource):

    @jwt_required
    def put(self, username):
        loggedUsername = get_jwt_identity()

        data = request.get_json()

        newTags = data.get('tags')

        current_user = mongo.db.users.find_one({'username': username})

        if not(loggedUsername == current_user.get('username') != None):
            return {
                'message': 'No cuenta con los permisos necesarios.',
                'success': 'false'}, 400
        else:
            if len(data.keys()) != 1:
                return {'message': 'Solo puede ingresar tags',
                        'success': 'false'}, 400
            else:
                updatedTags = []

                if current_user.get('tags') != None:
                    oldTags = current_user.get('tags')

                    for old_tag in oldTags:
                        updatedTags.append(old_tag)

                    for new_tag in newTags:
                        if newTags.count(new_tag) > 1:
                            return {'message': 'Tiene elementos repetidos',
                                    'success': 'false'}, 400

                        if new_tag in validTags:
                            updatedTags.append(new_tag)

                        else:
                            return {'message': 'Tags no son válidos',
                                    'success': 'false'}, 400

                    updatedTags = list(dict.fromkeys(updatedTags))

                else:
                    for new_tag in newTags:
                        if newTags.count(new_tag) > 1:
                            return {'message': 'Tiene elementos repetidos',
                                    'success': 'false'}, 400

                        if new_tag in validTags:
                            updatedTags.append(new_tag)

                        else:
                            return {'message': 'Tags no son válidos',
                                    'success': 'false'}, 400

                # Creamos el query para el nuevo status
                newValue = {"$set": {'tags': updatedTags}}

                # Obtenemos el usuario a modificar
                current_user = mongo.db.users.find_one(
                    {"username": loggedUsername})

                mongo.db.users.update_one(current_user, newValue)
                return {'message': 'Tags actualizados',
                        'content': {'tags': updatedTags},
                        'success': 'true'}, 200
