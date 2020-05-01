from pymongo import MongoClient
from utils.environment import Environment


class Connection():
    def __init__(self):
        config = Environment().settingsDB()
        client = MongoClient(config['DB_HOST'], config['DB_PORT'])
        self.database = client[config['DB_DATABASE']]
        # self.users = self.database.users

    # Metodo de prueba para sacar un registro mediante username
    def mostrarRegistro(self, username):
        return self.database.users.find_one(
            {"username": f'{username}'})

    # Metodo para actualizar un (1) usuario.
    # Este recibe el usuario a actualizar como user
    # y el valor a cambiar como newValue
    def updateUserData(self, user, newValue):
        return self.database.users.update_one(user, newValue)
        logging.info(x.modified_count, "Dato actualizado")
