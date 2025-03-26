valorRestaurante = float(input('Digite o valor da conta do restaurante: '))
porcentagemGorjeta = float(input('Digite a porcentagem da gorjeta: '))

valorFinal = valorRestaurante + (valorRestaurante * (porcentagemGorjeta / 100))

print(f'O valor para ser pago é de: {valorFinal}')