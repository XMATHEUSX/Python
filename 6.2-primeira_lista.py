Lista1 = []
Lista2 = []
Lista3 = []
while True:
    elemento = input("insira elementeos na lista 1:")
    if (elemento == "0"):
        while True:
            elemento = input("insira elementeos na lista 2:")
            if (elemento == "0"):
                break
            else:
                Lista2.append(elemento)
        break
    else:
        Lista1.append(elemento)
Lista3.extend(Lista1)
Lista3.extend(Lista2)
print(Lista3)
