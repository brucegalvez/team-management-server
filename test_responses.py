#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Librerias importadas
import unittest
import requests
import json

# Modulos propios
from main import app

BASE_URL = "http://localhost:8080"
SIGNUP_URL = f"{BASE_URL}/home/signup"
LOGIN_URL = f"{BASE_URL}/home/login"
PROFILE_URL = f"{BASE_URL}/me/profile"
STATUS_URL = f"{BASE_URL}/me/status"
FRIENDS_URL = f"{BASE_URL}/dashboard/friends"
FRIEND_URL = f"{BASE_URL}/dashboard/friends/1"


class SingupTest(unittest.TestCase):
    def setUp(self):
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_createUser(self):
        response = self.app.post(SIGNUP_URL)
        self.assertEqual(201, response.status_code)

    def test_loginUser(self):
        response = self.app.post(LOGIN_URL)
        self.assertEqual(201, response.status_code)

    def test_ProfileData(self):
        response = self.app.put(PROFILE_URL)
        self.assertEqual(204, response.status_code)

    def test_UserStatus(self):
        payload = json.dumps({
            "estado de conexion": "Conectado"
        })
        response = requests.put(STATUS_URL, headers={
                                "Content-Type": "application/json"}, data=payload)
        data = response.json()
        self.assertEqual(200, response.status_code)
        self.assertEqual("true", data["success"])

    def test_UserDashboard(self):
        response = self.app.get(FRIENDS_URL)
        self.assertEqual(200, response.status_code)

    def test_UserInfo(self):
        response = self.app.get(FRIEND_URL)
        self.assertEqual(200, response.status_code)
