# meu script
from random import randint
from re import I

soma = 0
count = 0
count_bot = 0

while True:
    bot = randint(0, 10)
    num = int(input("Digite um valor: "))
    jogador = str(input("Você quer PAR ou Ímpar? [P/I]: ")).strip().upper()
    print("-" * 35)

    if jogador not in "IiPp":
        jogador = str(input("Digite [P] para PAR e [I] para IMPAR "))

    soma = bot + num
    print("DEU PAR" if soma % 2 == 0 else "DEU IMPAR")
    print("-" * 35)

    if soma % 2 == 0:
        if jogador in "P":
            count += 1
            print(f"vocẽ jogou {num} e o computador {bot}. DEU {soma}")
            print("-" * 35)
            print("VOCE VENCEU!")
            print("-" * 35)
            print("Vamos jogar novamente?")
        else:
            count_bot += 1
            print(f"Você jogou {num} e o computador jogou {bot}. DEU {soma}")
            print("-" * 60)
            break
    if soma % 2 == 1:
        if jogador in "I":
            count += 1
            print(f"vocẽ jogou {num} e o computador {bot}. Deu {soma}")
            print("-" * 35)
            print("VOCE VENCEU!")
            print("Vamos jogar novamente?")
            print("-" * 35)
        else:
            count_bot += 1
            print(f"Você jogou {num} e o computador jogou {bot}. Deu {soma}")
            print("-" * 60)
            break
print(f"GAME OVER. você ganhou {count} vezes e o computador {count_bot} vezes")
print("-" * 60)

# script do professor

from random import randint

count = 0

while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = " "

    while tipo not in "PI":
        tipo = str(input("par ou impar? [P/I] ")).strip().upper()
    print(
        f"voce jogou {jogador} e o computador jogou {computador}. total de {total}",
        end="",
    )
    print("deu par" if jogador % 2 == 0 else "deu impoar")

    if tipo == "P":
        if total % 2 == 0:
            print("voce venceu")
            count += 1
        else:
            print("voce PERDEU")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("voce venceu")
            count += 1
        else:
            print("Voce perdeu")
            break
    print("vamos jogar novamente?...")
print("Game over. voce venceu {count} vezes.")
