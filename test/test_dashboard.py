#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import *


class DashboardTest(unittest.TestCase):
    def setUp(self):
        app.config['DEBUG'] = False
        app.config['MONGO_URI'] = 'mongodb://localhost:27017/intranet'
        self.app = app.test_client()
        # Creo dos usuarios en la DB y obtengo un token para el primero
        signUpKeys = ['birthday', 'campus', 'email', 'firstName',
                      'lastName', 'password', 'phone', 'username']
        self.app.post(
            SIGNUP_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(generateUser(idNum=1, filterKeys=signUpKeys)))
        self.app.post(
            SIGNUP_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(generateUser(idNum=2, filterKeys=signUpKeys)))
        response = self.app.post(
            LOGIN_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(generateUser(
                idNum=1, filterKeys=["email", "password"])))
        data = json.loads(response.data)
        self.token = data['content']['token']

    def test_userInfo_success(self):
        response = self.app.get(
            f"{FRIENDS_URL}/testUsername2",
            headers={"Content-Type": "application/json",
                     "Authorization": f"Bearer {self.token}"})
        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("true", data['success'])

    def test_userInfo_error(self):
        response = self.app.get(
            f"{FRIENDS_URL}/testUsername2",
            headers={"Content-Type": "application/json"})
        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("false", data['success'])

    def tearDown(self):
        return super().tearDown()
