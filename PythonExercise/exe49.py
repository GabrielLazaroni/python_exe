# tabuada usando laço for

'''valor = int(input('numero:'))
index = 0
print(f'tabuada de {valor}')

for i in range(0, 11):
    print(f'{index} X {valor} = {index * valor}')
    index = index + 1'''

num = int(input('digite um numero para: '))
for i in range(1, 11):
    print('{} x {:2} = {}'.format(num, i, num*i))