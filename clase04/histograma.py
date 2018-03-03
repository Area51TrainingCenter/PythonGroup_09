from PIL import Image, ImageDraw

imagen = Image.open('gatito.jpg')

# [0, 0, 0, 0, ...]
rojos = [0 for _ in range(256)]
verdes = [0 for _ in range(256)]
azules = [0 for _ in range(256)]

for rojo, verde, azul in imagen.getdata():
    rojos[rojo] += 1
    verdes[verde] += 1
    azules[azul] += 1


def crear_histograma(conteos, nombre_archivo, incremento):
    lienzo = Image.new('RGB', (255, 255), 'white')
    lapiz = ImageDraw.Draw(lienzo)

    maximo = max(conteos)
    color_linea = (0, 0, 0)
    for color, conteo in enumerate(conteos):
        punto_inicial = (color, 255)
        punto_final = (color, (255 - (conteo / maximo) * 255))
        lapiz.line([punto_inicial, punto_final], color_linea, 1)
        color_linea = incremento(color_linea)

    lienzo.save(nombre_archivo)


crear_histograma(
    rojos,
    'rojo.bmp',
    lambda color: (color[0] + 1, color[1], color[2])
)

crear_histograma(
    verdes,
    'verde.bmp',
    lambda color: (color[0], color[1] + 1, color[2])
)

crear_histograma(
    azules,
    'azul.bmp',
    lambda color: (color[0], color[1], color[2] + 1)
)
