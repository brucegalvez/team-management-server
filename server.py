#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Librerias importadas
from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from utils.environment import Environment

# Configuracion inicial de Flask
app = Flask(__name__)

# Configuracion del JWT
config = Environment().settingsJWT()
app.config['JWT_SECRET_KEY'] = config['JWT_SECRET_KEY']
app.config['JWT_ALGORITHM'] = config['JWT_ALGORITHM']
jwt = JWTManager(app)

bcrypt = Bcrypt(app)

api = Api(
    app,
    title='Pachaqtec Intranet',
    version='1.0',
    description='Backend de app para administración.'
)
