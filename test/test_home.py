#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import *


class HomeTest(unittest.TestCase):
    def setUp(self):
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_createUser(self):
        response = self.app.post(SIGNUP_URL)
        self.assertEqual(201, response.status_code)

    def test_loginUser(self):
        response = self.app.post(LOGIN_URL)
        self.assertEqual(201, response.status_code)

    def test_UserDashboard(self):
        response = self.app.get(FRIENDS_URL)
        self.assertEqual(200, response.status_code)

    def test_UserInfo(self):
        response = self.app.get(FRIEND_URL)
        self.assertEqual(200, response.status_code)
