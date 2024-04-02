"""
Exercício
Peça ao usuário para digitar seu nome
"""
nome = input('Digite seu nome: ')
# Peça ao usuário para digitar sua idade
idade = input('Digite sua idade: ')

if nome and idade:
  print('Seu nome é',nome)
  print('Seu nome invetido é',(nome[::-1]))
  print('Seu nome tem essa quantidade de',(len (nome[::])))

  if ' ' in nome:
       print(f'Seu nome tem espacos')
    
  else: 
     print(f'Seu nome nao tem espacos')

#         Seu nome tem {n} letras

#         A primeira letra do seu nome é {letra}

  print('A primeira letra do seu nome é',(nome[0]))

#         A última letra do seu nome é {letra}
  print('A ultima letra do seu nome é',(nome[-1]) )

else:
   print('Desculpe, você deixou campos vazios.')