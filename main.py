from flask import Flask, request
from random import *

app= Flask(__name__)

@app.route("/")
def home():
    return '''

<h1> Aplicación Calculadora </h1>

<p> Opciones Diponibles </p>

<ul>

    <li>
        <a href="/suma?a=8&b=12"> 
            Suma
        </a>
    </li>
    
    <li>
        <a href="/resta?a=8&b=12"> 
            Resta
        </a>
    </li>
    
    <li>
        <a href="/multiplicación?a=8&b=12"> 
            Multiplicación
        </a>
    </li>

    <li>
        <a href="/división?a=8&b=12"> 
            División
        </a>
    </li>

    <li>
        <a href="/división_p?a=8&b=12"> 
            División Piso
        </a>
    </li>

    <li>
        <a href="/random?a=8&b=12"> 
            Random
        </a>
    </li>

</ul>

'''

#Esta es una ruta adicional en la aplicación
@app.route("/suma")
def ruta_suma():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    R_suma= a+b
    
    return f''' 
        "La suma de los numeros {a} y {b} es: {R_suma} "
        <a href="/">Volver al inicio <a>
        '''

@app.route("/resta")
def ruta_resta():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    R_resta= a-b
    
    return f'''
        "La resta de los numeros {a} y {b} es: {R_resta} "
        <a href="/">Volver al inicio <a>
        '''

@app.route("/multiplicación")
def ruta_multiplicación():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    R_multiplicación= a*b
    
    return f'''
        "La multiplicación de los numeros {a} y {b} es: {R_multiplicación} "
        <a href="/">Volver al inicio <a>
        '''

@app.route("/división")
def ruta_división():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    R_división= a/b
    
    return f'''
        "La división de los numeros {a} y {b} es: {R_división}"
        <a href="/">Volver al inicio <a>
        '''

@app.route("/división_p")
def ruta_división_p():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    R_división_p= a//b
    
    return f"La división de los numeros {a} y {b} es: {R_división_p}"

@app.route("/random")
def ruta_random():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    random = uniform (a, b)
    
    return f"Numero randon entre {a} y {b} es: {random}"

#Esto nos permite actualizar rapidamente los cambios
if __name__=="__main__":
    app.run(debug=True)