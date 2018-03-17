from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    contexto = {
        'nombre': 'Rodrigo',
        'edad': 29,
        'amigos': ['luis', 'carlos', 'julio', 'pepe']
    }
    return render_template('index.html', **contexto)


@app.route('/saludo', methods=['GET', 'POST'])
def saludo():
    contexto = {}
    if request.method == 'POST':
        contexto['nombre'] = request.form.get('nombre')
    return render_template('saludo.html', **contexto)


app.run(debug=True)
