#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import *


class ProfileTest(unittest.TestCase):
    def setUp(self):
        app.config['DEBUG'] = False
        app.config['MONGO_URI'] = 'mongodb://localhost:27017/intranet'
        self.app = app.test_client()

        # Creamos un usuario en la DB y obtenemos su token
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

    def test_UserProfileData_good_all(self):

        payload = json.dumps({
            "profile": "Estudio en PachaQtec",
            "program": "FrontEnd",
            "campus": "Lima",
            "phone": "+51991467953",
            "campus": "Ate",
            "program": "BackEnd"
        })

        response = self.app.put(f'{PROFILE_URL}/testUsername1/profile',
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

        response = self.app.put(f'{PROFILE_URL}/testUsername1/profile',
                                headers={
                                    "Content-Type": "application/json",
                                    "authorization": f"Bearer {self.token}"},
                                data=payload)

        data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual("false", data['success'])

    def test_UserTags_good(self):

        payload = json.dumps({
            "tags": ["HTML", "CSS"]
        })

        response = self.app.put(f'{PROFILE_URL}/testUsername1/profile/tags',
                                headers={
                                    "Content-Type": "application/json",
                                    "authorization": f"Bearer {self.token}"},
                                data=payload)

        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("true", data['success'])

    def test_UserTags_bad_repeated(self):

        payload = json.dumps({
            "tags": ["HTML", "CSS", "CSS"]
        })

        response = self.app.put(f'{PROFILE_URL}/testUsername1/profile/tags',
                                headers={
                                    "Content-Type": "application/json",
                                    "authorization": f"Bearer {self.token}"},
                                data=payload)

        data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual("false", data['success'])

    def test_UserTags_bad_non_existent(self):

        payload = json.dumps({
            "tags": ["HT!ML", "CSSSSS"]
        })

        response = self.app.put(f'{PROFILE_URL}/testUsername1/profile/tags',
                                headers={
                                    "Content-Type": "application/json",
                                    "authorization": f"Bearer {self.token}"},
                                data=payload)

        data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual("false", data['success'])

    def test_UserTags_bad_more_keys(self):

        payload = json.dumps({
            "tags": ["HT!ML", "CSSSSS"],
            "Hello": "Want to broke this"
        })

        response = self.app.put(f'{PROFILE_URL}/testUsername1/profile/tags',
                                headers={
                                    "Content-Type": "application/json",
                                    "authorization": f"Bearer {self.token}"},
                                data=payload)

        data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual("false", data['success'])

    def tearDown(self):
        return super().tearDown()
