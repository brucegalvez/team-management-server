#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos propios
from server import *
from logger import *
from utils.lastConnection import *
from utils.environment import Environment

# Librerias importadas
from flask_restx import Resource
from flask import jsonify, request


class UserStatus(Resource):
    # Ruta para cambiar tu estado de conexion
    def put(self):
        config = Environment().settingsOptions()
        # Declaramos la lista de valores posibles
        status_list = config['STATUS_OPTIONS']

        # Capturamos la respuesta en una variable
        data = request.get_json()
        new_status = data["status"]

        # Validamos que el estado esté en la lista
        if new_status in status_list:
            if new_status == 'Conectado':
                return {
                    'status': new_status,
                    "success": "true"}, 200
            else:
                return {
                    'status': new_status,
                    'connection': f'Última conexión: {last_conection}',
                    "success": "true"}, 200
        else:
            return {
                'message': 'Elija una opción correcta',
                'success': 'false'}, 200


class UserProfileData(Resource):
    # Ruta para la API para editar perfil
    def put(self):
        return 'Cambio de informacion exitoso', 204
