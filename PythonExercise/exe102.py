from math import factorial

def fatorial(num, show=True):
    count = escolha
    fact = 1
    f = factorial(escolha)
    
    if show == False:
        print(f'O fatorial de {num} é = {f}')
    else:
        while count > 0:
            print(f'{count}', end='')
            print(' x ' if count > 1 else ' = ', end='')
            fact *= count
            count -= 1
        print(f'{fact}')


escolha = int(input('Escolha um numero para saber seu fatorial: '))
fatorial(escolha)
    