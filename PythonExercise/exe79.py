from time import sleep

valores = []

while True:
    num = int(input("Digite um valor: "))
    if num not in valores:
        valores.append(num)
        valores.sort()
        print("Valor adicionado!")
    else:
        print("Valor Dupicado...")

    resposta = str(input("Deseja continuar? [s/n]"))
    if resposta in "Nn":
        break

print("ANALISANDO... ")
sleep(3)
print(f"os numeros digitados, mostrando em ordem crescente sao: {valores}")
