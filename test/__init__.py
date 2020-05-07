#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Librerias importadas
from utils.environment import Environment
import unittest
import json

# Modulos propios
from application import app
from utils.userGenerator import UserGenerator
generateUser = UserGenerator().generateUser

BASE_URL = "http://localhost:8080"
SIGNUP_URL = f"{BASE_URL}/home/signup"
LOGIN_URL = f"{BASE_URL}/home/login"
CHAT_URL = f"{BASE_URL}/chat"
FRIENDS_URL = f"{BASE_URL}/dashboard/friends"
PROFILE_URL = f"{BASE_URL}/dashboard"
MONGO = Environment().settingsDB()
