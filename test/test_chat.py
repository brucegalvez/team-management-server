#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import *
from .test_home import HomeTest


class ProfileTest(unittest.TestCase):
    def setUp(self):
        app.config['DEBUG'] = False
        app.config['MONGO_URI'] = MONGO['MONGO_URI']
        self.app = app.test_client()

    def test_UserStatus_good(self):
        good_payload = json.dumps({'status': 'Conectado'})

        response = requests.put(STATUS_URL,
                                headers={
                                    "Content-Type": "application/json",
                                    "authorization": 'Bearer ' + str(TOKN['TOKEN'])},
                                data=good_payload)

        data = response.json()
        self.assertEqual(200, response.status_code)
        self.assertEqual("true", data['success'])

    def test_UserStatus_good(self):
        bad_payload = json.dumps({'status': 'asdgasdgasdgasd'})

        response = requests.put(STATUS_URL,
                                headers={
                                    "Content-Type": "application/json",
                                    "authorization": 'Bearer ' + str(TOKN['TOKEN'])},
                                data=bad_payload)

        data = response.json()
        self.assertEqual(400, response.status_code)
        self.assertEqual("false", data['success'])

    def test_ChatDisplay_good(self):
        good_payload = json.dumps({
            "username": "javicarden",
            "program": "FrontEnd"
        })

        response = requests.get(CHAT_URL,
                                headers={
                                    "Content-Type": "application/json",
                                    "authorization": 'Bearer ' + str(TOKN['TOKEN'])},
                                data=good_payload)

        data = response.json()
        self.assertEqual(200, response.status_code)
        self.assertEqual("true", data['success'])

    def test_ChatDisplay_bad(self):
        bad_payload = json.dumps({
            "username": "asdgasdgasdg",
            "program": "FrontEnd"
        })

        response = requests.get(CHAT_URL,
                                headers={
                                    "Content-Type": "application/json",
                                    "authorization": 'Bearer ' + str(TOKN['TOKEN'])},
                                data=bad_payload)

        data = response.json()
        self.assertEqual(400, response.status_code)
        self.assertEqual("false", data['success'])
