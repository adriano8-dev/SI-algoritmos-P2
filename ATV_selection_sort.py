def selection_sort(lista):
    for i in range(len(lista)):
        menor = i

        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]
    return lista
valores = [26, 64, 25, 13, 8, 2]
print(f'Lista original: {valores}')
print(f'lista ordenada: {selection_sort(valores)}')