while True:
    numero1 = input('Digite um numero: ')
    numero2 = input('Digite outro numero: ')
    operador = input('Digite um operador sendo, (+/-/*): ')
    
    numeros_validos = None

    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos numeros sao invalidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
         print('Operador invalido.')
         continue

    if len(operador) > 1 :
        print('Digite apenas um operador.')
        continue

    sair = input ('Quer sair? [s]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break