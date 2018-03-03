import requests

origen = input('Ingrese moneda origen: ')
destino = input('Ingrese moneda destino: ')
cantidad = float(input('Ingrese cantidad: '))
cambio = requests.get('https://api.fixer.io/latest',
                      params={'base': origen}).json()
origen = origen.upper()
destino = destino.upper()
print('{}: {}'.format(origen, cantidad * cambio['rates'][destino]))
