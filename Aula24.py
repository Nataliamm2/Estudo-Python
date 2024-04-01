# nome = 'Natália'
# # print(nome[-4])
# print('á' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
   print(f'{encontrar} esta em nome')

else: 
   print(f'{encontrar} nao esta em {nome}')