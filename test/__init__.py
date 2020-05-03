#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Librerias importadas
import unittest
import requests
import json
from random import randint

# Modulos propios
from main import app

BASE_URL = "http://localhost:8080"
SIGNUP_URL = f"{BASE_URL}/home/signup"
LOGIN_URL = f"{BASE_URL}/home/login"
STATUS_URL = f"{BASE_URL}/chat/<username>"
CHAT_URL = f"{BASE_URL}/chat"
FRIENDS_URL = f"{BASE_URL}/dashboard/friends"
FRIEND_URL = f"{BASE_URL}/dashboard/friends/1"
PROFILE_URL = f"{BASE_URL}/dashboard/<username>/profile"
