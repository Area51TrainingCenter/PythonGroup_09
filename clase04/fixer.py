import requests

cambio = requests.get('https://api.fixer.io/latest').json()

euros = float(input('Ingrese cantidad en EUROS: '))
dolares = (cambio['rates'])['USD'] * euros

print('DOLARES: {}'.format(dolares))
