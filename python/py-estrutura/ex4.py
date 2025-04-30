tupla = (1, 3, 5)

maior = tupla[0]

if tupla[1] > maior:
    maior = tupla[1]

    if tupla[2] > maior:
        maior = tupla[2]

print(maior)