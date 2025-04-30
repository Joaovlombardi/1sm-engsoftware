num_1 = float(input('Digite um valor: '))
num_2 = float(input('Digite outro valor: '))
num_3 = float(input('Digite mais um valor: '))

tupla = (num_1, num_2, num_3)

if tupla[0] < (tupla[1] + tupla[2]) and tupla[1] < (tupla[0] + tupla[2]) and tupla[2] < (tupla[0] + tupla[1]):
    print('É um triângulo!')
else:
    print('Não é um triângulo.')
