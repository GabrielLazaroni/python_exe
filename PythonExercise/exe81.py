lista = []

while True:
    num = lista.append(int(input("Digite um valor: ")))
    resposta = str(input("Deseja continuar? [s/n] ")).strip().upper()
    lista.sort(reverse=True)
    if resposta in "Nn":
        break

print(f"{len(lista)} numeros foram digitados")
print(f"a lista ordenada de forma decrescente fica: {lista}")
print(
    f"o valor 5 está na lista" if 5 in lista else print("o valor 5 nao está na lista")
)
