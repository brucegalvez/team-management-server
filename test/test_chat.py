#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import *


class ProfileTest(unittest.TestCase):
    def setUp(self):
        app.config['DEBUG'] = False
        app.config['MONGO_URI'] = 'mongodb://localhost:27017/intranet'
        self.app = app.test_client()
        # Creamos un usuarios en la DB y obtenemos su token
        signUpKeys = ["firstName", "lastName",
                      "username", "email", "password"]
        self.app.post(
            SIGNUP_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(generateUser(idNum=1, filterKeys=signUpKeys)))

        response = self.app.post(
            LOGIN_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(generateUser(
                idNum=1, filterKeys=["email", "password"])))

        data = json.loads(response.data)
        self.token = data['content']['token']

        self.app.put(
            f"{PROFILE_URL}/testUsername1/profile",
            headers={"Content-Type": "application/json",
                     "authorization": f"Bearer {self.token}"},
            data=json.dumps({'program': 'BackEnd'}))

    def test_UserStatus_good(self):
        good_payload = json.dumps({'status': 'Conectado'})

        response = self.app.put(
            f"{CHAT_URL}/testUsername1",
            headers={"Content-Type": "application/json",
                     "authorization": f"Bearer {self.token}"},
            data=good_payload)
        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("true", data['success'])

    def test_UserStatus_bad(self):
        bad_payload = json.dumps({'status': 'asdgasdgasdgasd'})

        response = self.app.put(f"{CHAT_URL}/testUsername1",
                                headers={
                                    "Content-Type": "application/json",
                                    "authorization": f'Bearer {self.token}'},
                                data=bad_payload)

        data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual("false", data['success'])

    def test_ChatDisplay_good(self):
        good_payload = json.dumps({
            "username": "testUsername1"
        })

        response = self.app.get(CHAT_URL,
                                headers={
                                    "Content-Type": "application/json",
                                    "authorization": f'Bearer {self.token}'},
                                data=good_payload)

        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("true", data['success'])

    def test_ChatDisplay_bad_username(self):
        bad_payload = json.dumps({
            "username": "asdgasdgasdg"
        })

        response = self.app.get(CHAT_URL,
                                headers={
                                    "Content-Type": "application/json",
                                    "authorization": f'Bearer {self.token}'},
                                data=bad_payload)

        data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual("false", data['success'])

    def tearDown(self):
        return super().tearDown()
