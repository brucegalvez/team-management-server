#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import *
from .test_home import HomeTest


class ProfileTest(unittest.TestCase):
    def setUp(self):
        app.config['DEBUG'] = False
        app.config['MONGO_URI'] = MONGO['MONGO_URI']
        self.app = app.test_client()

    def test_UserProfileData(self):

        payload = json.dumps({
            "profile": "Estudio en PachaQtec",
            "program": "FrontEnd",
            "campus": "Lima",
            "phone": "+51991467953",
            "email": "aho123@mail.com",
            "campus": "Ate",
            "program": "BackEnd"
        })

        response = requests.put(PROFILE_URL,
                                headers={
                                    "Content-Type": "application/json",
                                    "authorization": 'Bearer ' + str(TOKN['TOKEN'])},
                                data=payload)

        data = response.json()
        self.assertEqual(200, response.status_code)
        self.assertEqual("true", data['success'])

    def test_UserStatus(self):
        payload = json.dumps({
            "status": "Conectado"
        })
        response = requests.put(
            STATUS_URL,
            headers={
                "Content-Type": "application/json",
                "authorization": 'Bearer ' + str(TOKN['TOKEN'])},
            data=payload)

        data = response.json()
        self.assertEqual(200, response.status_code)
        self.assertEqual("true", data["success"])
