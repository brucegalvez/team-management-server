#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import *
from .test_home import HomeTest


class ProfileTest(unittest.TestCase):
    def setUp(self):
        app.config['DEBUG'] = False
        app.config['MONGO_URI'] = 'mongodb://localhost:27017/intranet'
        self.app = app.test_client()
        # Creo dos usuarios en la DB y obtengo un token para el primero
        signUpKeys = ["firstName", "lastName",
                      "username", "email", "password"]
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
                idNum=2, filterKeys=["email", "password"])))
        data = json.loads(response.data)
        self.token = data['content']['token']

    def test_UserProfileData_good_all(self):

        payload = json.dumps({
            "profile": "Estudio en PachaQtec",
            "program": "FrontEnd",
            "campus": "Lima",
            "phone": "+51991467953",
            "email": "aho123@mail.com",
            "campus": "Ate",
            "program": "BackEnd"
        })

        response = self.app.put(f'{PROFILE_URL}/testUsername2/profile',
                                headers={
                                    "Content-Type": "application/json",
                                    "authorization": f"Bearer {self.token}"},
                                data=payload)

        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("true", data['success'])

    def test_UserProfileData_bad_profile(self):

        payload = json.dumps({
            "profile": "Mas de 150 caracteres - Mas de 150 caracteres - Mas de 150 caracteres - Mas de 150 caracteres - Mas de 150 caracteres - Mas de 150 caracteres - Mas de 150 caracteres - ",
            "program": "FrontEnd",
            "campus": "Lima",
            "phone": "+51991467953",
            "email": "aho123@mail.com",
            "campus": "Ate",
            "program": "BackEnd"
        })

        response = self.app.put(f'{PROFILE_URL}/testUsername2/profile',
                                headers={
                                    "Content-Type": "application/json",
                                    "authorization": f"Bearer {self.token}"},
                                data=payload)

        data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual("false", data['success'])
