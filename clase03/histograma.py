from PIL import Image, ImageDraw

imagen = Image.open('gatito.jpg')

# 1: 100, 2: 300, ..
rojos = {}
verdes = {}
azules = {}

for rojo, verde, azul in imagen.getdata():
    if rojo not in rojos:
        rojos[rojo] = 1
    else:
        rojos[rojo] += 1

    if verde not in verdes:
        verdes[verde] = 1
    else:
        verdes[verde] += 1

    if azul not in azules:
        azules[azul] = 1
    else:
        azules[azul] += 1


def crear_histograma(conteos, nombre_archivo):
    lienzo = Image.new('RGB', (255, 255))
    lapiz = ImageDraw.Draw(lienzo)

    maximo = max(conteos.values())
    for color in range(256):
        conteo = conteos.get(color, 0)
        punto_inicial = (color, 255)
        punto_final = (color, (255 - (conteo / maximo) * 255))
        lapiz.line([punto_inicial, punto_final], 'white', 1)

    lienzo.save(nombre_archivo)


crear_histograma(rojos, 'rojo.bmp')
crear_histograma(verdes, 'verde.bmp')
crear_histograma(azules, 'azul.bmp')
