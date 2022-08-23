pessoas = []
dados = []
maior = menor = 0

while True:
    dados.append(str(input("Digite seu nome: ")))
    dados.append(float(input("Digite sua peso: ")))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    resp = str(input("Deseja continuar? [s/n]")).strip().upper()
    if resp in "N":
        break

print(f"{len(pessoas)} pessoas foram casdastradas.")

for i in pessoas:
    if i[1] == maior:
        print(f"A pessoa mais pesada é {i[0]}, com {maior}Kg")
    elif i[1] == menor:
        print(f"a pessoas mais leve é {i[0]}, com {menor}Kg")
