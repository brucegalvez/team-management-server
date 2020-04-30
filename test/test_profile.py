#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import *


class ProfileTest(unittest.TestCase):
    def setUp(self):
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_ProfileData(self):
        response = self.app.put(PROFILE_URL)
        self.assertEqual(204, response.status_code)

    def test_UserStatus(self):
        payload = json.dumps({
            "status": "Conectado"
        })

        response = requests.put(
            STATUS_URL,
            headers={
                "Content-Type": "application/json"},
            data=payload)

        data = response.json()
        self.assertEqual(200, response.status_code)
        self.assertEqual("true", data["success"])
        self.assertIsNotNone(payload["status"])
