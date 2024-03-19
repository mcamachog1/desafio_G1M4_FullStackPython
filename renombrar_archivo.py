import os
antiguo = os.path.join("logs", "error.txt")
nuevo = os.path.join("logs", "error.log")
os.rename(antiguo, nuevo)