#importando a biblioteca MATH

from math import factorial

num = int(input('Digite um valor: '))
f = factorial(num)
print(f'o fatorial de {num} é {f}')

# da meneira tradicional

num = int(input('digite um numero: '))
count = num
fact = 1
print('Calculando {}! = '.format(num), end='')

while count > 0:
    print('{}'.format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
    fact *= count
    count -= 1
print('{}'.format(fact))