# Ejemplo simple de comprehension de diccionarios

# Imprimir las ventas mayores a 'umbral'
umbral = 40000
ventas = {
 "Enero": 15000,
 "Febrero": 22000,
 "Marzo": 12000,
 "Abril": 17000,
 "Mayo": 81000,
 "Junio": 13000,
 "Julio": 21000,
 "Agosto": 41200,
 "Septiembre": 25000,
 "Octubre": 21500,
 "Noviembre": 91000,
 "Diciembre": 21000,
}

# Solución sin comprehension
meses_sobre_umbral = {}
for mes, venta in ventas.items():
    if venta > umbral:
        meses_sobre_umbral[mes] = venta
print("\nCiclo for tradicional")
print("Los meses por encima del umbral son: ", meses_sobre_umbral)

# Solución con comprehension
print("\nCiclo for con comprehension")
print("Los meses por encima del umbral son: ",{mes:venta for mes,venta in ventas.items() if venta > umbral})


