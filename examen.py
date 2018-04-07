from PIL import Image

colores = [
    ' ',
    '.',
    ',',
    "'",
    '"',
    'o',
    '\\',
    'H',
    '#',
    '@'
]


def imagen_a_ascii(ruta, ancho=50):
    imagen = Image.open(ruta)
    imagen.thumbnail((ancho, ancho))

    texto = ''
    for y in range(imagen.size[1]):
        for x in range(imagen.size[0]):
            r, g, b = imagen.getpixel((x, y))
            promedio = (r + g + b) / 3
            promedio = promedio / 255
            texto += colores[int(promedio * len(colores) - 1)]
        texto += '\n'

    return texto


archivo = open('imagen.txt', 'w')
archivo.write(imagen_a_ascii('imagen.jpg'))
archivo.close()
