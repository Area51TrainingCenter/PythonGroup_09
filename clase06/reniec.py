import requests
from PIL import Image

URL_BASE = 'https://cel.reniec.gob.pe/valreg/'

sesion = requests.Session()
sesion.get(URL_BASE + 'valreg.do')

respuesta_imagen = sesion.get(URL_BASE + 'codigo.do')
archivo = open('imagen.jpg', 'wb')
archivo.write(respuesta_imagen.content)
archivo.close()

imagen = Image.open('imagen.jpg')
ancho, alto = imagen.size

for x in range(ancho):
    for y in range(alto):
        color = imagen.getpixel((x, y))
        # si el color no es eminentemente azul
        if color > (13, 13, 180):
            imagen.putpixel((x, y), (255, 255, 255))

imagen.save('imagen2.jpg')
