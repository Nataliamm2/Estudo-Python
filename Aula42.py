frase = 'O Python é uma linguagem de programacao'\
'multiparadigma.'\
'Python foi criado pr Guido van Rossum.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ' '
while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
    
    quantas_apareceu_mais_vezes_atual = frase.count(letra_atual)
    
    if qtd_apareceu_mais_vezes < quantas_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = quantas_apareceu_mais_vezes_atual
        letra_que_apareceu_mais_vezes = letra_atual
         
    i += 1 
    
print(
    'A letra que apareceu mais vezes foi ' 
      f'"{letra_que_apareceu_mais_vezes}" que apareceu '
      f'{qtd_apareceu_mais_vezes} x'
      )