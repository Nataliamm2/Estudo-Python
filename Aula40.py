"""Calculadora com while"""

while True:
    sair = input ('Quer sair? [s]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break
