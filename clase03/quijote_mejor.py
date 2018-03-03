import re
archivo = open('quijote.txt', encoding='utf-8')
contenido = archivo.read()
archivo.close()

palabras = re.split(r'\s+', contenido.lower())
conteo = {}

for palabra in palabras:
    if palabra not in conteo:
        conteo[palabra] = 1
    else:
        conteo[palabra] += 1

el_mayor = ('', 0)
for palabra, veces in conteo.items():
    if veces > el_mayor[1]:
        el_mayor = (palabra, veces)

print(el_mayor)
