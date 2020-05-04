import re
from logger import *
#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Validate():
    def validateMobile(self, phone):

        # El numero que ingresa por parametro debe coincidir
        # con la siguiente regla de regex
        rule = re.compile('[+]519\d{8}$')

        if re.match(rule, phone):
            logging.debug(f"Número validado: {phone}")
            return True
        else:
            logging.debug(f'{phone} no es un número correcto')
            return False

    # El correo que ingresa por parametro debe coincidir
    # con la siguiente regla de regex
    def validateEmail(self, email):
        rule = re.compile('[a-zA-z0-9_.+-]+@[a-zA-Z-]+\.[a-z]+$')

        if re.match(rule, email):
            logging.debug(f"Correo validado: {email}")
            return True
        else:
            logging.debug(f'{email} no es un email correcto')
            return False

    def validatePassword(self, password):
        rule = re.compile('[A-Za-z0-9@#$%^&+=]{8,}')
        if re.match(rule, password):
            logging.debug(f"Contraseña validado: {password}")
            return True
        else:
            logging.debug(f'{password} no es una contraseña válida')
            return False

    def validateGivenName(self, givenName):
        rule = re.compile('[A-Za-z]{,45}')
        if re.match(rule, givenName):
            logging.debug(f"Nombre validado: {givenName}")
            return True
        else:
            logging.debug(f'{givenName} no es un Nombre válido')
            return False

    def validateUsername(self, username):
        rule = re.compile('[A-Za-z0-9]{,30}')
        if re.match(rule, username):
            logging.debug(f"Usuario validado: {username}")
            return True
        else:
            logging.debug(f'{username} no es un usuario válido')
            return False

    def validateProfile(self, profile):
        rule = re.compile("[^']{,150}$")

        if re.match(rule, profile):
            logging.debug(f"Perfil validado: {profile}")
            return True
        else:
            logging.debug(f'{profile} tiene más de 150 caracteres')
            return False
