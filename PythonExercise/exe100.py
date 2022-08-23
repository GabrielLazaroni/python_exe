from random import randint
from time import sleep

numeros = []


def sorteia():
    print("Os numero sortados são... ", end="")

    for i in range(0, 5):
        n = randint(0, 20)
        numeros.append(n)
        print(f"{n} ", end="", flush=True)
        sleep(0.2)
    print()


def soma_par():
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f"Sorteando o valores pares de {numeros} temos {soma}")


sorteia()
soma_par()
