#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos propios
from server import *
from logger import *
from utils.lastConnection import *
from utils.environment import Environment
from utils.dictChange import DictChange
from utils.validate import Validate


# Librerias importadas
import datetime
from flask import request, jsonify
from flask_restx import Resource
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

dictChange = DictChange()
validate = Validate()
getTime = GetTime()

# Declaramos la lista de status posibles
status_list = ["Conectado", "Ocupado",
               "Ausente", "No Disponible", "Desconectado"]

# Declaramos categorías de datos de perfil válidas
validFields = ["profile", "program", "phone",
               "email", "campus", "profile picture", "tags"]

# Declaramos lista de campus válidos
validCampus = ['Lima Centro', 'Wilson', 'San Juan de Miraflores',
               'San Juan de Lurigancho', 'Tomás Valle - Lima Norte', 'Ate - Lima Este']

# Declaramos lista de especialidades válidas
validPrograms = ['BackEnd', 'FrontEnd',
                 'Desarrollo de Apps Móviles',
                 'Diseño de Experiencia del Usuario']

# Declaramos lista de especialidades válidas
validTags = ['Python', 'Java', 'Javascript', 'C#', 'PHP',
             'C/C++', 'R', 'Objective-C', 'Swift', 'Matlab',
             'HTML', 'CSS', 'SQL', 'Bash/Shell/PowerShell',
             'TypeScript', 'JQuery', 'Angular/Angular.js',
             'React.js', 'ASP.NET', 'Express', 'Spring',
             'Vue.js', 'Django', 'Flask', 'Laravel',
             'Ruby on Rails', 'Drupal']
