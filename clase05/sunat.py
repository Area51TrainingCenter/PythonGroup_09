import pytesseract
import pyttsx3
import requests
from bs4 import BeautifulSoup
from PIL import Image

URL_BASE = 'http://www.sunat.gob.pe/cl-ti-itmrconsruc/'

sesion = requests.Session()
sesion.get(URL_BASE + 'jcrS00Alias')
respuesta = sesion.get(URL_BASE + 'frameCriterioBusqueda.jsp')

soup = BeautifulSoup(respuesta.content, 'html.parser')
url_img = URL_BASE + soup.find('img').attrs['src']

archivo_imagen = open('imagen.jpg', 'wb')
archivo_imagen.write(sesion.get(url_img).content)
archivo_imagen.close()

captcha = pytesseract.image_to_string(Image.open('imagen.jpg'))
print(captcha)

DNI = input('Ingrese DNI: ')

data = {
    'accion': 'consPorTipdoc',
    'razSoc': '',
    'nroRuc': '',
    'nrodoc': DNI,
    'contexto': 'ti-it',
    'search1': '',
    'codigo': captcha,
    'tQuery': 'on',
    'tipdoc': '1',
    'search2': DNI,
    'coddpto': '',
    'codprov': '',
    'coddist': '',
    'search3': ''
}

respuesta_consulta = sesion.post(URL_BASE + 'jcrS00Alias', data=data)

soup = BeautifulSoup(respuesta_consulta.content, 'html.parser')

resultado = soup.find_all('table')[5].find_all('tr')[1].text.strip()

print(resultado)
engine = pyttsx3.init()
engine.say(resultado)
engine.runAndWait()
