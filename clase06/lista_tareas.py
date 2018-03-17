from flask import Flask, render_template, request, redirect

app = Flask(__name__)


tareas = ['Trapear', 'Correr']


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        tareas.append(request.form['tarea'])
    return render_template('tareas.html', tareas=enumerate(tareas))


@app.route('/eliminar/<int:posicion>/', methods=['GET'])
def eliminar(posicion):
    del tareas[posicion]
    return redirect('/')


@app.route('/editar/<int:posicion>/', methods=['GET', 'POST'])
def editar(posicion):
    contexto = {
        'tarea': tareas[posicion]
    }

    if request.method == 'POST':
        tareas[posicion] = request.form['tarea']
        return redirect('/')

    return render_template('editar.html', **contexto)


app.run(debug=True)
