string = 'ABCDE' # 5 CARACTERES (len)

# .       0 .  1 .     2 .          3 .   4 .        5 .         6 .        7 .      
lista = [123, True, 'Luiz Otavio', 1.2, 'Robot', 'Cyprees', 'Selenium', 'Appium', []]
lista[-6] = 'Maria'
print(lista)
print(lista[-6], type(lista[-6]))


#print(bool([])) #falsy 