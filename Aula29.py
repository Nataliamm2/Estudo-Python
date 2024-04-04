numeros_str = input('Vou dobrar o numero que voce digitar: ')

try:
   print('STR:',numeros_str)
   numero_float = float(numeros_str)
   print('FLOAT:', numero_float)
   print(f'O dobro de {numeros_str} é {numero_float * 2}')

except:
    print('Isso não é um número')

# print(numeros_str.isdigit())

# numero_float = float(numeros_str)
# print(f'O dobro de {numeros_str} é {numero_float * 2}')
