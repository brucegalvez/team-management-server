# Importamos modulos para capturar el tiempo
import datetime

# Se utilizara para obtener la ultima conexión del usuario
x = datetime.datetime.now()
last_conection = x.strftime("%Y-%B-%A--%I:%M:%S %p")
