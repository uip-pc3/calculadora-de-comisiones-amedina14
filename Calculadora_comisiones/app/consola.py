"""
La empresa ABC está interesada en una calculadora de comisiones.
La calculadora de comisiones es una plataforma web que calcula cuánto dinero le corresponde a un vendedor dada las ventas mensuales.

ABC ha definido algunas reglas que indican cómo se distribuye la comisión:

Para ventas que superan los $100,000, el vendedor recibe una comisión del 15% de su total de ventas mensual.
Para ventas que superan los $75,000, el vendedor recibe una comisión del 10% de su total de ventas mensual.
Para ventas que superan los $50,000, el vendedor recibe una comisión del 7% de su total de ventas mensual.
Para ventas que superan los $25,000, el vendedor recibe una comisión del 5% de su total de ventas mensual.
Para el resto de ventas, el vendedor recibe una comisión del 3% de su total de ventas mensual.
En caso tal no se haya dado ventas en el mes, entonces el vendedor recibe un llamado de atención.
La plataforma web debe validar las entradas antes de procesar la solicitud, debe mostrar la salida
a través de una nueva página y guardar este resultado en un fichero CSV dentro del servidor
que siga el patrón "apellido,nombre,ventas,comision" (ejemplo: Martinez,Carlos,200000,30000).

No es necesario realizar pruebas unitarias, ni documentar. Igualmente, si lo hace, tendrá puntos adicionales.
"""
import csv, operator

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre",
         "Diciembre"]

ventas = []

file = open("file1.csv", "w+")

for sale in meses:
    comision = 0
    venta = float(input("Ingresa el monto en ventas: "))
    ventas.append(venta)
    if (venta > 100):
        comision = venta * 0.15
        tot = venta + comision
    elif (75 < venta <= 100):
        comision = venta * 0.10
        tot = venta + comision
    elif (50 < venta <= 75):
        comision = venta * 0.07
        tot = venta + comision
    elif (25 < venta <= 50):
        comision = venta * 0.05
        tot = venta + comision
    elif (0 < venta <= 25):
        comision = venta * 0.03
        tot = venta + comision
    elif (venta == 0):
        tot = "Señor, ud no ha realizado ventas este mes."

    print(str(tot))
    file.write(";")
    file.write(str(tot))
    file.write("\n")

try:
    file = open("file1.csv","a+")
# Array de Meses
    for mes in meses:

            print(mes)
#            print(str(tot))
            file.write(mes)
            file.write(";")
            file.write("\n")
            '''file.write(";")
            file.write(str(tot))'''

    '''
    for sale in meses:
        comision = 0
        venta = float(input("Ingresa el monto en ventas: "))
        ventas.append(venta)
        if (venta > 100):
            comision = venta * 0.15
            tot = venta + comision
        elif (75 < venta <= 100):
            comision = venta * 0.10
            tot = venta + comision
        elif (50 < venta <= 75):
            comision = venta * 0.07
            tot = venta + comision
        elif (25 < venta <= 50):
            comision = venta * 0.05
            tot = venta + comision
        elif (0 < venta <= 25):
            comision = venta * 0.03
            tot = venta + comision
        elif (venta == 0):
            tot = "Señor, ud no ha realizado ventas este mes."

        print(str(tot))

        file.write(";")
        file.write(str(tot))
        file.write("\n")
    '''

except FileNotFoundError:
    print("\nNo existe el file")

'''
try:
    file = open("file1.csv","a+")
#Array de ventas
    for sale in meses:
        comision = 0
        venta = float(input("Ingresa el monto en ventas: "))
        ventas.append(venta)
        if (venta > 100):
            comision = venta * 0.15
            tot = venta + comision
        elif (75 < venta <= 100):
            comision = venta * 0.10
            tot = venta + comision
        elif (50 < venta <= 75):
            comision = venta * 0.07
            tot = venta + comision
        elif (25 < venta <= 50):
            comision = venta * 0.05
            tot = venta + comision
        elif (0 < venta <= 25):
            comision = venta * 0.03
            tot = venta + comision
        elif (venta == 0):
            tot = "Señor, ud no ha realizado ventas este mes."

        print(str(tot))

        file.write(";")
        file.write(str(tot))
        file.write("\n")
#        file.write(";")
except FileNotFoundError:
    print("\nNo existe el file")
'''

print("\nDato guardado")

