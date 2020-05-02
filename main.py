#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Modulos propios
from utils.environment import Environment
from server import *
from logger import *
from controllers.homeController import UserCreator, LoginController
from controllers.dashboardController import UsersDashboard, UserInfo
from controllers.profileController import UserProfileData
from controllers.chatController import UserStatus


# Las siguientes funcionalidades
# inicializan la experiencia del usuario
home = api.namespace('home', description='Sign up & Login API')
home.add_resource(UserCreator, '/signup')
home.add_resource(LoginController, '/login')

# Las siguientes funciones aplican cambios dentro de tu perfil
profile = api.namespace('me', description='Profile API')
profile.add_resource(UserProfileData, '/<username>/profile')

# La siguiente api, recibe peticiones dentro del chat
chatroom = api.namespace('chat', description='Chat API')
chatroom.add_resource(UserStatus, '/<username>/status')

# Las siguientes funcionan se accionan desde un dashboard
dashboard = api.namespace('dashboard', description='Dashboard API')
dashboard.add_resource(UsersDashboard, '/friends')
dashboard.add_resource(UserInfo, '/friends/<int:id>')

if __name__ == '__main__':
    config = Environment().settingsGeneral()
    app.run(port=config['PORT'], debug=config['DEBUG'])
