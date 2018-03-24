from entidades import *

# @db_session
# def crear_tareas():
#     lista_tareas = [
#         'Lavar',
#         'Cocinar',
#         'Planchar',
#         'Correr',
#         'Comer',
#     ]
#
#     for nombre in lista_tareas:
#         t = Tarea(nombre=nombre)
#
#
# crear_tareas()

with db_session:
    lista_tareas = [
        'Lavar',
        'Cocinar',
        'Planchar',
        'Correr',
        'Comer',
    ]

    for nombre in lista_tareas:
        t = Tarea(nombre=nombre)
