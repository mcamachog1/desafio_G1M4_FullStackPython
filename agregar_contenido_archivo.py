from datetime import datetime
import os

try:
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    path = os.path.join("logs", "error.log")
    with open(path, "a+") as log:
        log.seek(0)
        print(log.read())
        now = datetime.now()
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")
        log.seek(0)
        print(log.read())