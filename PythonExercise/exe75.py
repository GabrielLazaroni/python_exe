num = (
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")),
)
print(f"voce digitou os valores {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3)+1}ª posição")
else:
    print("O valor 3 nao foi encontrado em nenhuma posiçao")
for i in num:
    if i % 2 == 0:
        print(f"os valores pares digitados foram {i}")
