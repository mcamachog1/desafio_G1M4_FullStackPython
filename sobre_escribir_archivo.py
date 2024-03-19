import os

try:
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    path = os.path.join("logs", "ultimo_error.log")
    with open(path,"r+") as log:
        log.write(f"ERROR: {e}")