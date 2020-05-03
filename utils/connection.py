from pymongo import MongoClient
from utils.environment import Environment


class Connection():
    def __init__(self):
        config = Environment().settingsDB()
        client = MongoClient(config['DB_HOST'], config['DB_PORT'])
        self.database = client[config['DB_DATABASE']]

    # Metodo para obtener un registro
    def showItem(self, key, value):
        return self.database.users.find_one(
            {key: value})

    # Metodo para actualizar un (1) registro.
    # Este recibe el usuario a actualizar como user
    # y el valor a cambiar como newValue
    def updateItem(self, user, newValue):
        return self.database.users.update_one(user, newValue)
