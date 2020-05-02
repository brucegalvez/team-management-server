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
            logging.info(f"Número validado: {phone}")
            return True
        else:
            logging.error(f'{phone} no es un número correcto')
            return False

    # El correo que ingresa por parametro debe coincidir
    # con la siguiente regla de regex
    def validateEmail(self, email):
        rule = re.compile('[a-zA-z0-9_.+-]+@[a-zA-Z-]+\.[a-z]')

        if re.match(rule, email):
            logging.info(f"Correo validado: {email}")
            return True
        else:
            logging.error(f'{email} no es un email correcto')
            return False
