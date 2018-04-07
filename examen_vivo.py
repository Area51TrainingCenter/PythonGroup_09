from PIL import Image

imagen = Image.open('imagen.jpg')
imagen.thumbnail((80, 80))

texto = ''
colores = [
    '@',
    '#',
    '%',
    '$',
    'B',
    '/',
    ',',
    '.',
    ' ',
]

for y in range(imagen.size[1]):
    for x in range(imagen.size[0]):
        r, g, b = imagen.getpixel((x, y))
        color = (r + g + b) / 3
        texto += colores[
            int(color / 255 * (len(colores) - 1))
        ]
    texto += '\n'

archivo = open('imagen.txt', 'w')
archivo.write(texto)
archivo.close()
