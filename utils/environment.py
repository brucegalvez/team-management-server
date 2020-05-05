#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.util import strtobool
import os
import utils.envi


class Environment():

    def settingsGeneral(self):
        return{
            'PORT': int(os.environ["PORTAPI"]),
            'DEBUG': strtobool(os.environ['DEBUG'])
        }

    def settingsDB(self):
        return{
            'MONGO_URI': os.environ["MONGO_URI"],
            'MONGO_TEST': os.environ['MONGO_TEST']}

    def settingsJWT(self):
        return {
            'JWT_SECRET_KEY': os.environ["JWT_SECRET_KEY"],
            'JWT_ALGORITHM': os.environ["JWT_ALGORITHM"]}
