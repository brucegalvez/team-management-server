#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import *


class HomeTest(unittest.TestCase):
    def setUp(self):
        app.config['DEBUG'] = False
        app.config['MONGO_URI'] = 'mongodb://localhost:27017/intranet'
        self.app = app.test_client()
        self.app.post(
            SIGNUP_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(self.generateUser(1))
        )

    def generateUser(self, idNum=randint(0, 9999), filterKeys=None):
        userTemplate = {
            "firstName": "testName",
            "lastName": "testName",
            "username": f"testUsername{idNum}",
            "email": f"testEmail{idNum}@testEmail.com",
            "password": "testPassword"
        }
        if filterKeys:
            return {k: v for k, v in userTemplate.items() if k in filterKeys}
        else:
            return userTemplate

    def test_createUser_success(self):
        response = self.app.post(
            SIGNUP_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(self.generateUser())
        )
        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("true", data['success'])

    def test_createUser_error(self):
        response = self.app.post(
            SIGNUP_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(self.generateUser(1, ["email"]))
        )
        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("false", data['success'])

    def test_loginUser_success(self):
        response = self.app.post(
            LOGIN_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(self.generateUser(1, ["email", "password"]))
        )
        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("true", data['success'])

    def test_loginUser_error(self):
        response = self.app.post(
            LOGIN_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(self.generateUser(1, ["email"]))
        )
        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("false", data['success'])

    def tearDown(self):
        return super().tearDown()
