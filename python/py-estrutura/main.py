#number = int(input('Digite um número:'))

#if number > 7:
#    print('Número maior que 7')

#----------

#numero = int(input('Digite um número:'))

#if numero >= 6:
#    print('Você foi aprovado!')
#else:
#    print('Você foi reprovado!')

#----------

#number = int(input('Digite um número:'))

#if number != 7:
#    print('Esse número não é o correto!')
#else:
#    print('Esse número é o correto!')

#----------

#print("Banana" > "Avelã")
#print("a" > "b")

#----------

#nota = float(input('Digite sua nota: '))

#if nota >= 6:
#    print('Aprovado')
#elif nota >= 5:
#    print('Exame')
#else:
#    print('Reprovado')

#----------

#a = 5
#b = 7
#c = 8

#if c > a or (a / 0):
#    print('Não pode dividir por zero')

#if  c > b and a < b:
#    print("Verdadeiro")
#else:
#    print("Falso")

#----------

#Estruturas de repetição:

#lista = ['j','b', 'c', 'd']

#for i, c in enumerate(lista):
#    print(i,':',c)

#if 'a' in lista:
#    print('Tem a letra A na lista')
#else:
#    print('Não tem a letra A na lista')

#--------------

#for i in range(0,50):
#    if i == 21:
#        break
#    print(i)
#
#for i in range(0, 30):
#    if i % 2 == 0:
#        continue
#    print(i)


#-------------------

#for i in range(0,50):
#    if i == 20:
#        print("Encontrei")
#        break
#    else: ##esse else é do for e não do if
#        print("Não encontrei")

#-----------------

#pares = [i for i in range(0,101) if i % 2 == 0]

#for i in range(0, 101, 2):
#        pares.append(i)

#print(pares)

#------------

#currentNumber = 0
#
#while currentNumber <= 10:
#    print(currentNumber)
#    currentNumber += 1

#---------------

#while True:
#    entrada = input('Digite algo: ')
#    if entrada == 'quit':
#        break
#    else:
#        print('O texto digitado foi:' + entrada)