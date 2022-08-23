primeiro = int(input("digite o termo: "))
razao = int(input("digite a razao: "))
count = 1
termo = primeiro
total = 0
mais = 10

while mais != 0:
    total += mais
    while count <= total:
        print("{} > ".format(termo), end="")
        termo += razao
        count += 1
    print("pausa")
    mais = int(input("quantos termos voce quer mostrar a mais? "))

print("FIM")
