
number = input('digite um numero: ')

print(f'unidade: {number[3]}')
print(f'dezena: {number[2]}')
print(f'centena: {number[1]}')
print(f'milhar: {number[0]}')

num = int(input('digite um numero: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print(f'unidade: {uni}')
print(f'dezena: {dez}')
print(f'centena: {cen}')
print(f'milhar: {mil}')



