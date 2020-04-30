#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos propios
from server import *
from logger import *
from lastConection import *

# Librerias importadas
from flask_restx import Resource
from flask import jsonify, request


class UserStatus(Resource):
    # Ruta para cambiar tu estado de conexion
    def put(self):
        
        # Declaramos la lista de valores posibles
        estados = ['Conectado', 'Ocupado', 'Ausente',
                   'No Disponible', 'Desconectado']
        
        # Capturamos la respuesta en una variable
        data = request.get_json()
        nuevo_estado = data["estado de conexion"]
        
        # Validamos que el estado esté en la lista
        if nuevo_estado in estados:
            return {
                'message': f'Tu nuevo estado de conexion es: {nuevo_estado}',
                'connection': f'Ultima conexion: {last_conection}',
                "success": "true"}, 200
        else:
            return {
                'message': 'Elija una opción correcta',
                'success': 'false'}, 200


class UserProfileData(Resource):
    # Ruta para la API para editar perfil
    def put(self):
        return 'Cambio de informacion exitoso', 204
