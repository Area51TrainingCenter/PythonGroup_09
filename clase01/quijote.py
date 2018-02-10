archivo = open('quijote.txt')
contenido = archivo.read()
archivo.close()

contenido = contenido.lower()

# {'e': _, 'l': _, 'i': _, 'n': _, 'g': _, 'e': _, ...}
letras = {}

for letra in contenido:
    if letra in 'abcdefghijklmnñopqrstuvwxyz':
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1

letras_ordenadas = sorted(letras.items(), key=lambda i: i[1], reverse=True)
#    'e'    238423  [('e', 83423), ('l', 39240923), ....]
for letra, veces in letras_ordenadas:
    print('{}: {}'.format(letra, veces))
