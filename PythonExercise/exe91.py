from random import randint
from time import sleep
from operator import itemgetter

dicionario = {}
ranking = []

dicionario["jogador1"] = randint(1, 6)
dicionario["jogador2"] = randint(1, 6)
dicionario["jogador3"] = randint(1, 6)
dicionario["jogador4"] = randint(1, 6)

print("-" * 30)
print("  == GIRANDO O DADO ==")
sleep(1)

for k, v in dicionario.items():
    print(f"    {k} tirou {v}")
    sleep(1)

ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)

print("-" * 30)
print("  == RANKING GANHADORES ==  ")

for i, v in enumerate(ranking):
    print(f"  {i}º lugar: {v[0]} com {v[1]}")
    sleep(1)
print("-" * 30)
