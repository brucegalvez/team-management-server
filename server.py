#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Librerias importadas
from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(
    app,
    title='Pachaqtec Intranet',
    version='1.0',
    description='Backend de app para administración.'
)
