# Comentario
cuantas_notas = float(input('Cuantas notas? '))

notas = 0

for n in range(cuantas_notas):
    notas += float(input('Nota {}: '.format(n + 1)))

promedio = notas / cuantas_notas
print('Promedio: {}'.format(promedio))

if promedio > 10.45:
    print('Aprobaste')
else:
    print('No aprobaste :(')
