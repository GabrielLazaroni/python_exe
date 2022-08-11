from random import randint
from time import sleep

# minha logica
bot_num = randint(0, 2)
palpite = 3
count = 0
print('VOCÊ CONSEGUE VENCER O COMPUTADOR?')

while palpite != bot_num:
    palpite = int(input('Digite um numero: '))
    count += 1
    if palpite < bot_num:
        print('Mais... tente mais uma vez: ')
    elif palpite > bot_num:
        print('menos... tente mais uma vez: ')
        
    print('Vamos analisar seu palpite...')
    sleep(2)

print('voce ganhou!')
print('{} palpites foram necessarios para acertar o numero!'.format(count))

#logica do professor

'''computador = randint(0, 10)
print('sou seu computador... acabei de pensar em numero entre 0 e 10.')
print('será que voce consegue adivinhar qual foi? ')
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez: ')
        elif jogador > computador:
            print('menos... tente mais uma vez: ')
print('Acertou com {} tentativas!'.format(palpites))'''