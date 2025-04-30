primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))
terceira_nota = float(input("Digite sua terceira nota: "))

media = (primeira_nota + segunda_nota + terceira_nota) / 3

if media >= 7:
    print(f'Aprovado com nota {media:.2f}')
else:
    print(f'Reprovado com nota {media:.2f}')