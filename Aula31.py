# v1 = 'a'
# v2 = 'b'
# print(id(v1))
# print(id(v2))

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faca algo')
else:
    print('nao faca algo')

# print(passou_no_if, passou_no_if is None)
# print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('Nao passou no if')

if passou_no_if is not None:
    print('Passou no if')

# print(id(v2))
