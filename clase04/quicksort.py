def quicksort(lista):
    if len(lista) == 0:
        return []

    if len(lista) == 1:
        return lista

    primer_elemento = lista[0]
    menores = [x for x in lista if x < primer_elemento]
    mayores = [x for x in lista if x > primer_elemento]
    return quicksort(menores) + [primer_elemento] + quicksort(mayores)


print(quicksort([4, 1, 3, 2, 6, 5]))
