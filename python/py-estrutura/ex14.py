num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

lista = [num1, num2]

if lista[0] > lista[1]:
    print(f'{lista[0]} é maior que {lista[1]}')
elif lista[0] < lista[1]:
    print(f'{lista[0]} é menor que {lista[1]}')
else:
    print(f'{lista[0]} e {lista[1]} são iguais!')
