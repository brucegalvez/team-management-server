import os
from dotenv import load_dotenv
from distutils.util import strtobool
load_dotenv()


class Environment():

    def settingsGeneral(self):
        return{
            'PORT': int(os.getenv("PORTAPI", 8081)),
            'DEBUG': strtobool(os.getenv('DEBUG', "false"))
        }
