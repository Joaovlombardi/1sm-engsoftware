mes = input("Digite algum mês do ano: ".upper())

match mes:
    case 'janeiro':
        print("O mês tem 31 dias")
    case 'fevereiro':
        print("O mês tem 28 dias")
    case 'março':
        print("O mês tem 31 dias")
    case 'abril':
        print("O mês tem 30 dias")
    case 'maio':
        print("O mês tem 31 dias")
    case 'junho':
        print("O mês tem 30 dias")
    case 'julho':
        print("O mês tem 31 dias")
    case 'agosto':
        print("O mês tem 31  dias")
    case 'setembro':
        print("O mês tem 30 dias")
    case 'outubro':
        print("O mês tem 31 dias")
    case 'novembro':
        print("O mês tem 30 dias")
    case 'dezembro':
        print("O mês tem 31 dias")
    case _:
        print('Digite um mês válido  ')