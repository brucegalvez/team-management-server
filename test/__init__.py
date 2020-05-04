#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Librerias importadas
import unittest
import requests
import json
from random import randint

# Modulos propios
from main import app
from utils.environment import Environment

BASE_URL = "http://localhost:8080"
SIGNUP_URL = f"{BASE_URL}/home/signup"
LOGIN_URL = f"{BASE_URL}/home/login"
STATUS_URL = f"{BASE_URL}/chat/javicarden"
CHAT_URL = f"{BASE_URL}/chat"
FRIENDS_URL = f"{BASE_URL}/dashboard/friends"
FRIEND_URL = f"{BASE_URL}/dashboard/friends/1"
PROFILE_URL = f"{BASE_URL}/dashboard/javicarden/profile"
TOKN = Environment().settingsRequest()
MONGO = Environment().settingsDB()
