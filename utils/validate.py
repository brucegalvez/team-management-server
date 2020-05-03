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
        rule = re.compile('[a-zA-z0-9_.+-]+@[a-zA-Z-]+\.[a-z]')

        if re.match(rule, email):
            logging.debug(f"Correo validado: {email}")
            return True
        else:
            logging.debug(f'{email} no es un email correcto')
            return False

    def validatePassword(self, password):
        rule = re.compile('[A-Za-z0-9@#$%^&+=]{8,}')
        return re.match(rule, password)

    def validateGivenName(self, givenName):
        rule = re.compile('[A-Za-z]{,45}')
        return re.match(rule, givenName)

    def validateUsername(self, username):
        rule = re.compile('[A-Za-z0-9]{,30}')
        return re.match(rule, username)
