#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Librerias importadas
import unittest
import json

# Modulos propios
from main import app

BASE_URL = "http://localhost:8080"
BASE_URL_SIGNUP = f"{BASE_URL}/home/signup"
BASE_URL_LOGIN = f"{BASE_URL}/home/login"


class SingupTest(unittest.TestCase):
    def setUp(self):
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_createUser(self):
        response = self.app.post(BASE_URL_SIGNUP)
        self.assertEqual(201, response.status_code)

    def test_loginUser(self):
        response = self.app.post(BASE_URL_LOGIN)
        self.assertEqual(201, response.status_code)
