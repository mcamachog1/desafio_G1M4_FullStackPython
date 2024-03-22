from error import EdadError

intentos = 0


while intentos <= 3:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad < 0:
            raise EdadError("Debe ser un numero positivo", edad)
        divisor = int(input("Ingrese número para dividir su edad:\n"))
        print(edad / divisor)
    except ValueError:
        print("Debe ingresar un número")
    except ZeroDivisionError:
        print("El número por el cual desea dividir no puede ser cero")
    except EdadError as e:
        print(f"La edad {e.edad} no es válida. {e.mensaje}")
    except Exception as e:
        print(f"ERROR:  {e}")
    finally:
        intentos += 1