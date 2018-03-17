from flask import Flask

app = Flask(__name__)


@app.route('/operacion/<nombre>/<float:a>/<float:b>')
def operacion(nombre, a, b):
    operaciones = {
        'suma': lambda x, y: x + y,
        'resta': lambda x, y: x - y,
        'producto': lambda x, y: x * y,
        'cociente': lambda x, y: x / y,
        'potencia': lambda x, y: x ** y,
    }

    return str(operaciones[nombre](a, b))


app.run(debug=True)
