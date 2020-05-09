from random import randint
import datetime


class UserGenerator():
    def generateUser(self, idNum=randint(0, 9999), filterKeys=None):
        userTemplate = {
            "firstName": "testName",
            "lastName": "testName",
            "username": f"testUsername{idNum}",
            "email": f"testEmail{idNum}@testEmail.com",
            "password": "testPassword",
            "profile": "testProfile",
            "program": "FrontEnd",
            "campus": "Lima Centro",
            "phone": "+51999999999",
            "birthday": "2018-06-12"
        }
        if filterKeys:
            return {k: v for k, v in userTemplate.items() if k in filterKeys}
        else:
            return userTemplate
