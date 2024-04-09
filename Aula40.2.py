while True:
    numero1 = input('Digite um numero: ')
    numero2 = input('Digite outro numero: ')
    operador = input('Digite um operador sendo, (+/-/*): ')
    
    num_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        num_validos = True
        
    except:
        num_validos = None

    if num_validos is None:
        print('Um ou ambos numeros sao invalidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
         print('Operador invalido.')
         continue

    if len(operador) > 1 :
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado: ')
    if operador == '+': 
        print(f'{num1_float}+{num2_float}=', num1_float + num2_float) 
    elif operador == '-': 
        print(f'{num1_float}-{num2_float}=', num1_float - num2_float)
    elif operador == '/':
        print(f'{num1_float}/{num2_float}=', num1_float / num2_float) 
    elif operador == '*':
        print(f'{num1_float}*{num2_float}=', num1_float * num2_float)
    else:
      print('Nunca deveria chegar aqui')

    sair = input ('Quer sair? [s]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break