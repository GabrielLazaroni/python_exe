from math import factorial

def fatorial(num, show=True):
    """
    A funçao fatorial recebe dois parametros (argumentos)
     => parametro num = é o numero que o usuario escolheu
     => parametro show = Recebe True or False. True para reber um output da esquação fatorial por extenso e False comente o resultado
    """
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
fatorial(escolha, show=True)
