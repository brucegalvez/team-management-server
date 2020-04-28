#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from utils.environment import Environment

app = Flask(__name__)

#Ruta para la API de login
@app.route('/signup', methods=['POST'])
def signup():
    return 'Este es la ruta para crear un nuevo usuario'

#Ruta para la API de validar la contraseña con Json Token
@app.route('/login')
def login():
    return 'Este es la ruta para validar la contraseña'

#Ruta para la API para editar perfil
@app.route('/edit-profile', methods=['PUT'])
def editProfile():
    return 'Este es la ruta para editar los datos de tu perfil'

#Ruta para la API para listar a los usuarios
@app.route('/list-users')
def listUsers():
    return 'Este es la ruta para mostrar usuarios'

#Ruta para la API
@app.route('/see-user')
def seeUser():
    return 'Este es la ruta a para ver los datos de un usuario'

@app.route('/change-status', methods=['PUT'])
def changeStatus():
    return 'Aquí podrás cambiar tu estado de conexión'


if __name__ == '__main__':
    config = Environment().settingsGeneral()
    app.run(port=config['PORT'], debug=config['DEBUG'])
