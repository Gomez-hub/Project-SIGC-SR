from datetime import datetime #se obtiene la fecha y la hora actual para registrar el evento en el log

class Logger: #registra eventos en un archivo de texto llamado logs.txt

    @staticmethod #No se necesita crear un objeto para usar el metodo
    def registrar_evento(mensaje): #reciba un texto

        with open("logs.txt", "a", encoding="utf-8") as archivo: #abre el archivo logs.txt en modo de escritura (append) para agregar nuevos eventos sin borrar los anteriores

            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #obtiene la fecha y hora actual y la formatea como una cadena en el formato "YYYY-MM-DD HH:MM:SS"

            archivo.write(f"[{fecha}] {mensaje}\n") #escribe el mensaje en el archivo logs.txt