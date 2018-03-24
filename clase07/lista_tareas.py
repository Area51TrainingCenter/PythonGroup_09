from flask import Flask, render_template, request, redirect, jsonify
from entidades import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@db_session
def home():
    if request.method == 'POST':
        t = Tarea(nombre=request.form['tarea'])

    return render_template('tareas.html', tareas=select(t for t in Tarea))


@app.route('/eliminar/<int:posicion>/', methods=['GET'])
@db_session
def eliminar(posicion):
    Tarea[posicion].delete()
    return redirect('/')


@app.route('/editar/<int:posicion>/', methods=['GET', 'POST'])
@db_session
def editar(posicion):
    contexto = {
        'tarea': Tarea[posicion]
    }

    if request.method == 'POST':
        Tarea[posicion].nombre = request.form['tarea']
        return redirect('/')

    return render_template('editar.html', **contexto)


@app.route('/tareas_json')
@db_session
def tareas_json():
    tareas = select(t for t in Tarea)
    return jsonify([
        {'id': tarea.id, 'nombre': tarea.nombre}
        for tarea in tareas
    ])


app.run(debug=True)
