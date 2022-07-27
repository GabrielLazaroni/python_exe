# construindo uma tabuada usando while

valor = int(input('numero:'))
index = 0
print(f'tabuada de {valor}')

while(index<=10):
    print(f'{index} X {valor} = {index * valor}')
    index = index + 1
