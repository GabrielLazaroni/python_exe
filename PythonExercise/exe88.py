from random import randint
from time import sleep

lista = []
jogos = []

print('-' * 51)
quant = int(input('Digite a quantidade de jogos você deseja gerar: '))
print('-' * 51)
total = 1

while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'SORTEANDO {quant} JOGOS...')

for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l} ')
    sleep(1)
print('-' * 51)