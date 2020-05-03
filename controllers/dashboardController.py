#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos propios
from . import *


class UsersDashboard(Resource):

    # Ruta para la API para listar a los usuarios
    def get(self):
        connected = []
        disconnected = []
        for user in connection.showList("status", "Conectado"):
            # connected.append(user['username'])
            username = user['username']
            firstName = user['firstName']
            lastName = user['lastName']
            lastConnection = user['lastConnection']
            connected.append(

                f"{firstName} {lastName} ({username}) Conectado: {lastConnection}")

        for user in connection.showList("status", "Desconectado"):
            # connected.append(user['username'])
            username = user['username']
            firstName = user['firstName']
            lastName = user['lastName']
            lastConnection = user['lastConnection']
            disconnected.append(
                f"{firstName} {lastName} ({username}) Desconectado: {lastConnection}")

        return f'Están conectados: {connected}. \
            Están desconectados: {disconnected}'


class UserInfo(Resource):
    # Ruta para obtener los datos de un solo usuario
    def get(self, id):
        return f'Este es la ruta a para ver los datos del usuario {id}', 200
