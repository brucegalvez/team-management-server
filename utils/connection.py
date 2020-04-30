from pymongo import MongoClient
from utils.environment import Environment


class Connection():
    def __init__(self):
        config = Environment().settingsDB()
        client = MongoClient(config['DB_HOST'], config['DB_PORT'])
        self.database = client[config['DB_DATABASE']]
