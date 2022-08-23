tupla = (
    "zero",
    "um",
    "dois",
    "tres",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezesete",
    "dezoito",
    "dezenove",
    "vinte",
)

while True:
    num = int(input("Digite um numero entre 0 e 20: "))
    if 0 <= num <= 20:
        print(f"voce digitou o numero {tupla[num]}")
    else:
        continue

    continuar = str(input("Deseja continuar? [s/n]")).strip().upper()
    if continuar in "Ss":
        continue
    else:
        break
print("obrigado por usar nosso programa!")
