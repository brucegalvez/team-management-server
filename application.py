#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Modulos propios
from utils.environment import Environment
from server import *
from logger import *
from controllers.homeController import UserCreator, LoginController
from controllers.dashboardController import UsersDashboard, UserInfo
from controllers.profileController import UserProfileData, UserTags
from controllers.chatController import UserStatus, ChatDisplay


# Las siguientes funcionalidades
# inicializan la experiencia del usuario
home = api.namespace('home', description='Sign up & Login API')
home.add_resource(UserCreator, '/signup')
home.add_resource(LoginController, '/login')


# Las siguientes funcionan se accionan desde un dashboard
dashboard = api.namespace('dashboard', description='Dashboard API')
dashboard.add_resource(UsersDashboard, '/friends')
dashboard.add_resource(UserInfo, '/friends/<username>')
dashboard.add_resource(UserProfileData, '/<username>/profile')
dashboard.add_resource(UserTags, '/<username>/profile/tags')

# La siguiente api, recibe peticiones dentro del chat
chatroom = api.namespace('chat', description='Chat API')
chatroom.add_resource(UserStatus, '/<username>')
chatroom.add_resource(ChatDisplay, '')

if __name__ == '__main__':
    config = Environment().settingsGeneral()
    app.run(host=config['HOST'], port=config['PORT'], debug=config['DEBUG'])
