"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# entrada = input('Digite um numero: ')

# if entrada.isdigit():
#     entrada_int =int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'impar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O numero digitado {entrada_int} é {par_impar_texto}')
# else: 
#     print('Voce nao digitou um valor numerico')

entrada = input('Digite um numero: ')

try:
    entrada_int =int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O numero digitado {entrada_int} é {par_impar_texto}')
except: 
    print('Voce nao digitou um valor numerico')



"""
Faça um programa que parte do primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
“Seu nome é normal”; maior que 6 escreva "Seu nome é muito grande".
"""