import logging

# configura logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)-15s %(funcName)-15s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='develop.log',
                    filemode='w')

# crea y asigna handler para imprimir en la consola
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(filename)-15s %(funcName)-15s %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
