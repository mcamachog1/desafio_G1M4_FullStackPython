from campania import Campania
from datetime import date

c = Campania("Campaña Demo", date.today(), date.today(), [
{"tipo": "video", "url_clic": "sin-url", "url_archivo": "sin-url",
"sub_tipo": "instream", "duracion": 30}
])

try:
    nombre = input("Ingrese nuevo nombre de la campaña:\n")
    sub_tipo = input("Ingrese nuevo sub tipo del anuncio:\n")
    c.nombre = nombre
    c.anuncios[0].sub_tipo = sub_tipo
except Exception as e:
    with open("error.log", "a+") as log:
        log.write(f"{e}\n")

print(c)