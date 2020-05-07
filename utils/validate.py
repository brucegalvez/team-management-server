import re
from logger import *
import datetime
#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Validate():
    def validateMobile(self, phone):

        # El numero que ingresa por parametro debe coincidir
        # con la siguiente regla de regex
        rule = re.compile('[+]519\d{8}$')

        if re.match(rule, phone):
            logging.debug("Número validado:")
            return True
        else:
            logging.debug('No es un número correcto')
            return False

    # El correo que ingresa por parametro debe coincidir
    # con la siguiente regla de regex
    def validateEmail(self, email):
        rule = re.compile('[a-zA-z0-9_.+-]+@[a-zA-Z-]+\.[a-z]+$')

        if re.match(rule, email):
            logging.debug("Correo validado")
            return True
        else:
            logging.debug('No es un email correcto')
            return False

    def validatePassword(self, password):
        rule = re.compile('[A-Za-z0-9@#$%^&+=]{8,}')
        if re.match(rule, password):
            logging.debug("Contraseña validado")
            return True
        else:
            logging.debug('No es una contraseña válida')
            return False

    def validateGivenName(self, givenName):
        rule = re.compile('[A-Za-z]{,45}')
        if re.match(rule, givenName):
            logging.debug("Nombre validado")
            return True
        else:
            logging.debug('No es un Nombre válido')
            return False

    def validateUsername(self, username):
        rule = re.compile('[A-Za-z0-9]{,30}')
        if re.match(rule, username):
            logging.debug("Usuario validado")
            return True
        else:
            logging.debug('No es un usuario válido')
            return False

    def validateProfile(self, profile):
        rule = re.compile("[^']{,150}$")

        if re.match(rule, profile):
            logging.debug("Perfil validado")
            return True
        else:
            logging.debug('Tiene más de 150 caracteres')
            return False

    def validateCampus(self, campus):
        validCampus = ['Lima Centro', 'Wilson', 'San Juan de Miraflores',
                       'San Juan de Lurigancho', 'Tomas Valle - Lima Norte', 'Ate - Lima Este']
        if campus in validCampus:
            logging.debug("Campus validado")
            return True
        else:
            logging.debug('El campus usado no existe')
            return False

    def validateBirthday(self, birthday):
        if type(birthday) is datetime.datetime:
            logging.debug("La fecha de cumpleaños ha sido validada")
            return True
        else:
            logging.debug('La fecha no es válida')
            return False
