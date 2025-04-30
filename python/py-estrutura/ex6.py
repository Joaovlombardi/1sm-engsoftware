lista = ['Sol', 'Solar', 'Solaridade']

num_carac_1 = len(lista[0])
num_carac_2 = len(lista[1])
num_carac_3 = len(lista[2])

if num_carac_1 > num_carac_2 and num_carac_1 > num_carac_3:
    print(f'A string maior é {lista[0]} com {num_carac_1} caracteres.')
elif num_carac_2 > num_carac_3 and num_carac_2 > num_carac_1:
    print(f'A string maior é {lista[1]} com {num_carac_2} caracteres.')
elif num_carac_3 > num_carac_1 and num_carac_3 > num_carac_2:
    print(f'A string maior é {lista[2]} com {num_carac_3} caracteres.')

