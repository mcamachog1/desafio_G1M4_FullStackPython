

import json
import os
from datetime import datetime
from usuario import Usuario

instancias = []

with open("usuarios.txt") as usuarios:
    linea = usuarios.readline()
    while linea:
        try:
            usuario = json.loads(linea)
            instancias.append(Usuario(usuario.get("nombre"), usuario.get("apellido"),usuario.get("email"), usuario.get("genero"))) 
            linea = usuarios.readline()
        except Exception as e:
            path = os.path.join("logs", "error.log")
            with open(path, "a+") as log:
                log.seek(0)
                now = datetime.now()
                log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")
        finally:
          linea = usuarios.readline()  

for usuario in instancias:
    print(f"Nombre del usuario: {usuario.nombre}, Apellido: {usuario.apellido}, Email: {usuario.email}, Genero: {usuario.genero} ") 


