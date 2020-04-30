#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Librerias importadas
import unittest
import requests
import json

# Modulos propios
from main import app

BASE_URL = "http://localhost:8080"
SIGNUP_URL = f"{BASE_URL}/home/signup"
LOGIN_URL = f"{BASE_URL}/home/login"
PROFILE_URL = f"{BASE_URL}/me/profile"
STATUS_URL = f"{BASE_URL}/me/status"
FRIENDS_URL = f"{BASE_URL}/dashboard/friends"
FRIEND_URL = f"{BASE_URL}/dashboard/friends/1"
