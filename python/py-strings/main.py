#texto = 'O resultado de 7 + 5 é :'
#soma = 7 + 5
#print(texto, soma)

###

#numero=10
#texto='o valor é: %d’ % numero'

###

#print(texto)
#print ('Agora são %02d:%02d.' % (16, 30))
#print ('Percentagem: %.1f%%, Exponencial:%.2e' % (5.333, 0.00314))
#print ('Decimal: %d, Octal: %o, Hexadecimal: %x' % (10, 10, 10))

#nome = 'Thon'
#sobre = 'de Souza'
#print("{} {}".format(nome, sobre))

#nome2 = 'Thon'
#sobre2 = 'de Souza'
#print("{:>20} {}".format(nome2, sobre2))

#nome3 = 'João Vitor'
#sobre3 = 'Lombardi'
#print(nome3, sobre3)

###

#resultado = 10 * 2
#texto = 'O valor de {} vezes {} é igual a: {}'.format(10, 2, resultado)

###

#numero1 = int(input("Digite um número: "))
#numero2 = int(input("Digite um segundo número: "))

#resultado = numero1 + numero2

#print('O resultado de {} + {} = {}'.format(numero1, numero2, resultado))

###

#numero1 = int(input("Digite um número: "))
#numero2 = int(input("Digite um segundo número: "))

#resultado = numero1 * numero2

#texto = f'O valor de {resultado} ao quadrado é {10**2}'
#texto = f'O valor de {resultado:.2f} ao quadrado é {resultado **2}'
#print(texto)

###

#s = "Olá, mundo!"
# Tamanho de uma string.
#number = len(s)
#print(number)

#s = 'Olá mundo!'

#s1 = s.replace("mundo", "céu")
#print(s1)

#s = 'AAAAAAAAAAAAA'

#s1 = s.replace("A", "py")
#print(s1)

###

#s = "Olá, mundo!"
# A string s começa com "Olá"?
#print(s.startswith("Olá"))
# A string s termina com "mundo!"?
#print(s.endswith("mundo!"))
# Quantas ocorrências da palavra "mundo" a string s possui?
#print(s.count("mundo"))

###

# Como "capitalizar" (transformar a primeira letra da primeira palavra em maiúscula).
#s = "ordem e progresso"
#print(s.capitalize())
# Como verificar se uma string só possui números.
#print('12345'.isdigit())
#print('12345abc'.isdigit())
# Como verificar se uma string é alfanumérica (possui letras e números).
#print('12345abc'.isalnum())

###

#String.find: procura uma substring em uma string e retorna o índice:
#s = "Pedro, Paulo e Maria"
#print(s.find("a"))
#Além disso, ela recebe um argumento adicional que especifica o índice pelo qual ela deve começar sua procura:
#print(s.find("a", 10))
#Ord: Retorna o valor decimal de um caractere
#print(ord('J'))
#chr: retorna o caractere de um valor decimal.
#print(chr(97))

###

#s='João é legal'
#print(s.title())
#print(s.lower())
#print(s.upper())

###

#texto='isso é '
#texto2=' um texto'
#print(texto+texto2)
#texto=texto.rstrip()
#texto2=texto2.lstrip()
#print(texto+texto2)

#s = "Olá, mundo!"
#print(s[-1])
#print(s[-2])

###

#frase = 'bando de aluno legal'

#print(frase[8:20])
##print(frase[-1])
#print(frase[0::2])

#pablinReação = "ah"
#niboReação = "Será que estuprar puta é crime?"

#print(f'A reação do paplin foi.. "{pablinReação}", já a reação do nibo foi.. "{niboReação}"')

###

#frase = "Boas pessoal sou um estudante"
#palavras = frase.split()
#print(palavras)

#print(','.join(palavras[::-1]))
#print(' '.join(['Oi', 'sumido']))

###

tabela = str.maketrans('aeiou', '1@*&%')
print('Vai Corinthians!'.translate(tabela))