# jogo para acertar qual numero o bot pensou

from random import randint
from time import sleep

num = int(input('escolha um numero e tente acertar qual numero o bot pensou: '))
num_bot = randint(1,2)

print('PROCESSANDO...')
sleep(2)

print('o numero escolhido pelo bot foi {}:'.format(num_bot))

if num == num_bot:
    print('voce acertou!!!')
else:
    print('voce perdeu! tente outra vez') 

