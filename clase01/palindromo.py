palabra = input('Escribe una palabra: ')

if palabra[::-1] == palabra:
    print('Sí es palíndromo')
else:
    print('No es palíndromo')
