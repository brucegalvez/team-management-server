#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import *


class HomeTest(unittest.TestCase):
    def setUp(self):
        app.config['DEBUG'] = False
        app.config['MONGO_URI'] = 'mongodb://localhost:27017/intranet'
        self.app = app.test_client()
        self.signUpKeys = ['birthday', 'campus', 'email', 'firstName',
                           'lastName', 'password', 'phone', 'username']
        self.logInKeys = ["email", "password"]
        self.app.post(
            SIGNUP_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(generateUser(idNum=1, filterKeys=self.signUpKeys)))

    def test_createUser_success(self):
        response = self.app.post(
            SIGNUP_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(generateUser(filterKeys=self.signUpKeys)))
        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("true", data['success'])

    def test_createUser_error(self):
        response = self.app.post(
            SIGNUP_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(generateUser(idNum=1, filterKeys=["email"])))
        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("false", data['success'])

    def test_loginUser_success(self):
        response = self.app.post(
            LOGIN_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(generateUser(
                idNum=1, filterKeys=self.logInKeys)))
        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("true", data['success'])

    def test_loginUser_error(self):
        response = self.app.post(
            LOGIN_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(generateUser(idNum=1, filterKeys=["email"])))
        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("false", data['success'])

    def tearDown(self):
        return super().tearDown()
