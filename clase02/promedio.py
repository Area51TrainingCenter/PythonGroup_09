def promedio(lista_notas):
    lista_notas.append(3)
    return sum(lista_notas) / len(lista_notas)


notas = [15, 16, 19]
el_promedio = promedio(notas)
print(notas)
print(el_promedio)
