# Importamos modulos para capturar el tiempo
import datetime

# Se utilizara para obtener la ultima conexión del usuario
x = datetime.datetime.now()
last_connection = x.strftime("%Y-%B-%A-%d--%I:%M:%S %p")
