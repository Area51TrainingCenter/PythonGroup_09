from flask import Flask

app = Flask(__name__)


@app.route('/')
def hola():
    return 'Hola Mundo!'


@app.route('/saludo')
def saludo():
    return 'Hola Pepito!'


@app.route('/saludar/<nombre>/')
def saludar(nombre):
    return 'Hola {}!'.format(nombre)


@app.route('/sumar/<int:a>/<int:b>/')
def sumar(a, b):
    return '{}'.format(a + b)


# /operacion/suma/3/5
# /operacion/resta/3/5
# /operacion/producto/3/5
# /operacion/cociente/3/5

app.run(debug=True)
