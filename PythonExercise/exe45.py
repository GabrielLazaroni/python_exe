from random import randint
from time import sleep

lista = ("Pedra", "Papel", "Tesoura")

valor_bot = randint(0, 2)

valor = int(
    input(
        """

MENU:

[0] Pedra
[1] Papel
[2] Tesoura

escolha uma das opçoes: """
    )
)

print("o computador escolheu {}".format(lista[valor_bot]))
print("você escolheu {}".format(lista[valor]))


if valor_bot == 0:

    if valor == 0:
        print("empate!")

    elif valor == 1:
        print("VOCE VENCEU!")

    elif valor == 2:
        print("VOCE PERDEU!")

    else:
        print("ação invalida")

elif valor_bot == 1:

    if valor == 1:
        print("EMPATE!")

    elif valor == 0:
        print("VOCE PERDEU!")

    elif valor == 2:
        print("VOCE VENCEU")

elif valor_bot == 2:

    if valor == 2:
        print("EMPATE!")

    elif valor == 0:
        print("VOCE VENCEU!")

    elif valor == 1:
        print("VOCE PERDEU!")

    else:
        print("ação invalida")
