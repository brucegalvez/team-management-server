#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
from distutils.util import strtobool
load_dotenv()


class Environment():

    def settingsGeneral(self):
        return{
            'PORT': int(os.getenv("PORTAPI", 8081)),
            'DEBUG': strtobool(os.getenv('DEBUG', "false"))
        }

    def settingsDB(self):
        return{
            'DB_HOST': os.getenv("DB_HOST", '127.0.0.1'),
            'DB_PORT': int(os.getenv("DB_PORT", 3306)),
            'DB_DATABASE': os.getenv("DB_DATABASE", 'intranet')
        }

    def settingsOptions(self):
        return {'STATUS_OPTIONS': list((os.getenv("STATUS_OPTIONS")).split('-')),
                'USER_DATA_OPTIONS': list((os.getenv("USER_DATA_OPTIONS")).split('-'))}

    def settingsJWT(self):
        return {
            'JWT_SECRET_KEY': os.getenv("JWT_SECRET_KEY"),
            'JWT_ALGORITHM': os.getenv("JWT_ALGORITHM"),
        }
