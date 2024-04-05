# """
# Faça um programa que exige a hora ao usuário e, baseando-se no horário
# descrito, exiba a saudação correspondente. Ex.
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
# """

entrada = input('Digite a hora em numeros inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
       print('Bom dia!')
             
    elif hora >= 12 and hora <= 17:
       print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
       print('Boa noite!')
    else:
       print('Nao conheco essa hora')
except:
    print('Por favor, digite hora apenas com numeros inteiros.')