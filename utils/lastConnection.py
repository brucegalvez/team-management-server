# Importamos modulos para capturar el tiempo
import datetime


class GetTime():
    def getTime(self):
        # Se utilizara para obtener la ultima conexión del usuario
        x = datetime.datetime.now()
        return x.strftime("%Y-%B-%A-%d--%I:%M:%S %p")
