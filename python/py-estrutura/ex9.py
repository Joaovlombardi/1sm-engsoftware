num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

lista = [num1, num2]

if lista[0] % lista[1] == 0:
    print('O número é divisível')
elif lista[0] % lista[1] != 0:
    print('O número não é divisivel')