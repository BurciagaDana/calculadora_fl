from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    mensaje = """
    <h1>Calculadora  Python </h1>
    <h2>click en  las siguientes rutas para realizar operaciones:</h2>
    <ul>
        <li>Suma: <code>/sumar/valor1/valor2</code></li>
        <li>Resta: <code>/restar/valor1/valor2</code></li>
        <li>Multiplicación: <code>/multiplicar/valor1/valor2</code></li>
        <li>División: <code>/dividir/valor1/valor2</code></li>
        <li>Máximo: <code>/mayor/valor1/valor2</code></li>
    </ul>
    """
    # Buricaga Renteria Dana Paola
    return mensaje

@app.route('/sumar/<num1>/<num2>')
def sumar(num1, num2):
    resultado = int(num1) + int(num2)
    return f"<h3>Resultado de la suma: {resultado}</h3>"

@app.route('/restar/<num1>/<num2>')
def restar(num1, num2):
    resultado = int(num1) - int(num2)
    return f"<h3>Resultado de la resta: {resultado}</h3>"

@app.route('/multiplicar/<num1>/<num2>')
def multiplicar(num1, num2):
    resultado = int(num1) * int(num2)
    return f"<h3>Resultado de la multiplicación: {resultado}</h3>"

@app.route('/dividir/<num1>/<num2>')
def dividir(num1, num2):
    divisor = int(num2)
    if divisor == 0:
        return "<h3>Error: No se puede dividir entre cero.</h3>"
    resultado = int(num1) / divisor
    return f"<h3>Resultado de la división: {resultado}</h3>"

@app.route('/mayor/<num1>/<num2>')
def mayor(num1, num2):
    valor1 = int(num1)
    valor2 = int(num2)
    maximo = max(valor1, valor2)
    return f"<h3>El número mayor entre {valor1} y {valor2} es {maximo}</h3>"

if __name__ == '__main__':
    app.run(debug=True)
