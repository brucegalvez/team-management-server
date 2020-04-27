from flask import Flask
from utils.environment import Environment

app = Flask(__name__)

if __name__ == '__main__':
    config = Environment().settingsGeneral()
    app.run(port=config['PORT'], debug=config['DEBUG'])
