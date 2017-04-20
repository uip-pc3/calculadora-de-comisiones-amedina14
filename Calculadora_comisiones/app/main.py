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
La plataforma web debe validar las entradas antes de procesar la solicitud, debe mostrar la salida a través de una nueva página y guardar este resultado en un fichero CSV dentro del servidor que siga el patrón "apellido,nombre,ventas,comision" (ejemplo: Martinez,Carlos,200000,30000).

No es necesario realizar pruebas unitarias, ni documentar. Igualmente, si lo hace, tendrá puntos adicionales.
"""

from flask import Flask
from flask import render_template
from flask import request
#from flask import

app = Flask(__name__)

def filegenerate(datos):
    with open('ventasForm.csv', 'a+') as file:
        for informacion in datos:
            file.write(informacion+",")
        file.write('\n')
    file.close()

meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
         9: "Septiembre", 10: "Octubre",
         11: "Noviembre", 12: "Diciembre"}
ventas = []
c=0
@app.route('/')
def index():
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
             "Noviembre", "Diciembre"]
    for mes in meses:
        return render_template('index.html', mes=mes)
        #mes=mes+str(1)

@app.route('/m1')
def m1():
    meses = {2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
         9: "Septiembre", 10: "Octubre",
         11: "Noviembre", 12: "Diciembre"}
    for mes in list(meses.values()):
        return render_template('index.html', mes=mes)

@app.route('/m2')
def m2():
    meses = {3:"Marzo"}
    for mes in list(meses.values()):
        return render_template('index.html', mes=mes)

@app.route('/m3')
def m3():
    meses = {4:"Abril"}
    for mes in list(meses.values()):
        return render_template('index.html', mes=mes)

@app.route('/m4')
def m4():
    meses = {5:"Mayo"}
    for mes in list(meses.values()):
        return render_template('index.html', mes=mes)

@app.route('/m5')
def m5():
    meses = {6:"Junio"}
    for mes in list(meses.values()):
        return render_template('index.html', mes=mes)

@app.route('/m6')
def m6():
    meses = {7:"Julio"}
    for mes in list(meses.values()):
        return render_template('index.html', mes=mes)

@app.route('/m7')
def m7():
    meses = {8:"Agosto"}
    for mes in list(meses.values()):
        return render_template('index.html', mes=mes)

@app.route('/m8')
def m8():
    meses = {9:"Septiembre"}
    for mes in list(meses.values()):
        return render_template('index.html', mes=mes)

@app.route('/m9')
def m9():
    meses = {10:"Octubre"}
    for mes in list(meses.values()):
        return render_template('index.html', mes=mes)

@app.route('/m10')
def m10():
    meses = {11:"Noviembre"}
    for mes in list(meses.values()):
        return render_template('index.html', mes=mes)

@app.route('/m11')
def m11():
    meses = {12:"Diciembre"}
    for mes in list(meses.values()):
        return render_template('index.html', mes=mes)

@app.route('/resultado', methods=['POST'])
def meses():
    if request.method == 'POST':
        name = request.form['name']
        apellido = request.form['apellido']
        venta = float(request.form['venta'])
        if venta!='' :
            if (venta > 100000): comision = 0.15
            elif (75000 < venta <= 100000): comision = 0.10
            elif (50000 < venta <= 75000): comision = 0.07
            elif (25000 < venta <= 50000): comision = 0.05
            elif (0 < venta <= 25000): comision = 0.03
            else:
                atencion = "Ud. no ha realizado ventas este mes"
                return render_template('resultado.html', atencion=atencion)
            comision= venta * comision

            meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
                     "Noviembre", "Diciembre"]
            info = [name,apellido,str(venta),str(comision)]
            filegenerate(info)
            for me in meses:
                mes=me
                #return render_template('resultado.html', mes=mes)
                return render_template('resultado.html', venta=venta, name=name, apellido=apellido, comision=comision, mes=mes)

            else:
                return render_template('error.html')

if __name__=="__main__":
    app.run(debug=True)