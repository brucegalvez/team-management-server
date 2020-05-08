from random import randint
import datetime


class UserGenerator():
    def generateUser(self, idNum=randint(0, 9999), filterKeys=None):
        x = datetime.datetime.now()
        userTemplate = {
            "firstName": "testName",
            "lastName": "testName",
            "username": f"testUsername{idNum}",
            "email": f"testEmail{idNum}@testemail.com",
            "password": "testPassword",
            "profile": "testProfile",
            "program": "FrontEnd",
            "campus": "Lima Centro",
            "phone": "+51999999999",
            "birthday": f'{x}'
        }
        if filterKeys:
            return {k: v for k, v in userTemplate.items() if k in filterKeys}
        else:
            return userTemplate
