#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Librerias importadas
from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from utils.environment import Environment

# Configuracion inicial de Flask
app = Flask(__name__)
env = Environment()

# Configuracion del JWT
settingsJWT = env.settingsJWT()
app.config['JWT_SECRET_KEY'] = settingsJWT['JWT_SECRET_KEY']
app.config['JWT_ALGORITHM'] = settingsJWT['JWT_ALGORITHM']
jwt = JWTManager(app)

# Configuracion de Pymongo
settingsDB = env.settingsDB()
app.config['MONGO_URI'] = settingsDB['MONGO_URI']
mongo = PyMongo(app)

bcrypt = Bcrypt(app)
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(
    app,
    title='Pachaqtec Intranet',
    version='1.0',
    description='Backend de app para administración.'
)
