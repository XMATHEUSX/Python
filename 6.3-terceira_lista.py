lista1 = [5, 1, 5, 2, 3, 2]
lista2 = [1, 13, 4, 5, 1, 2, 5]
lista = []
n = 0
i = 1
lista.extend(lista1)
lista.extend(lista2)
while n <= len(lista)-1:
    i = n+1
    while i <= len(lista)-1:
        if lista[n] == lista[i]:
            del lista[i]
        i += 1
    n += 1
print(lista)
