#def saudacao(nome):
#    '''
#    ESSA FUNÇÃO SERVE PARA CHAMAR O SEU NOME!
#    '''
#    return f"Olá {nome}"

#mensagem = saudacao('João Vitor')

#print(mensagem)

#------------------------------

#def calcMedia(nota1, nota2, nota3):
#    media = (nota1 + nota2 + nota3) / 3

#    return media

#------------------------------

#print(calcMedia(10, 10, 10))

#def calcmedia2(notas):
#    media = sum(notas) / len(notas)
#    return media

#print(calcmedia2([10, 10, 10]))

#------------------------------

#def calcular_media(a, b):
#    return (a + b) / 2

#nota1 = int(input('Digite sua primeira nota: '))
#nota2 = int(input('Digite sua segunda nota: '))

#media = calcular_media(nota1, nota2)
#print(media)

#------------------------------

#def somar(a, b):
#    return a + b

#args = [3, 5]

#resultado = somar(*args) # Usa * para desempacotar a lista
#print(resultado)

#kwargs = {'a': 3, 'b': 5}

#resultado = somar(**kwargs) # Usa ** para desempacotar o dicionário
#print(resultado)

#------------------------------

#def somar(a = 2, b = 3):
#    return a + b

#resultado = somar(5,4)

#print(resultado)

#------------------------------

#def criar_usuario(nome, idade=18, cidade="São Paulo"):
#    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

#criar_usuario("Ana") # Saída: Nome: Ana, Idade: 18, Cidade: São Paulo
#criar_usuario("Pedro", 25) # Saída: Nome: Pedro, Idade: 25, Cidade: São Paulo
#criar_usuario("Clara", 30, "Rio de Janeiro") # Saída: Nome: Clara, Idade: 30, #Cidade: Rio de Janeiro

#def alterar_a(a):
#    a = a + 1
#    print(a)

#a = 2
#alterar_a(a)
#print(a)

#------------------------------

#def alterar_lista(lista):
#    lista.append(2)
#    lista.append(5)
#
#    print(lista)
#
#lista = [1,7,8,3]
#
#alterar_lista(lista[:])
#
#print(lista)

#------------------------------

#def soma_total(*numeros):
#    """
#    Esta função aceita um número arbitrário de argumentos e retorna a soma de
#    todos.
#    """
#    return sum(numeros)

#print(soma_total(1, 2, 3))
#print(soma_total(10, 20, 30, 40))
#print(soma_total())

#------------------------------

def exibir_infos(**infos):
    for chave, valor in infos.items():
        print(f"{chave}, {valor}")

exibir_infos(nome="Ana", idade=25, cidade="São Paulo")
print("---------")
exibir_infos(produto="Notebook", preco=2500.00, marca="Dell")




