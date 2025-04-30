num1 = int(input('Insira um número: '))
num2 = int(input('Insira um número: '))
num3 = int(input('Insira um número: '))

tupla = (num1, num2, num3)

if tupla[0] == tupla[1] == tupla[2]:
    print('Os números são iguais!')
elif tupla[0] != tupla[1] and tupla[0] != tupla[2] and tupla[1] != tupla[2]:
    print('Os números são diferentes!')
else:
    print('Dois números são iguais!')
