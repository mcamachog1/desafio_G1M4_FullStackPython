class Usuario():
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.genero = genero

import json
instancias = []

with open("usuarios.txt") as usuarios:
    linea = usuarios.readline()
    while linea:
        usuario = json.loads(linea)
        instancias.append(Usuario(usuario.get("nombre"), usuario.get("apellido"),usuario.get("email"), usuario.get("genero"))) 
        linea = usuarios.readline()

for usuario in instancias:
    print(f"Nombre del usuario: {usuario.nombre}, Apellido: {usuario.apellido}, Email: {usuario.email}, Genero: {usuario.genero} ") 