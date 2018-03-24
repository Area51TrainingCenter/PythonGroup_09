from pony.orm import *

db = Database()


class Tarea(db.Entity):
    nombre = Required(str)


db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
