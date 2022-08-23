count = count_f = count_m = 0

while True:
    idade = int(input("Qual a sua idade? "))
    if idade >= 18:
        count += 1

    sexo = str(input("Qual o seu sexo: [F/M]")).strip().upper()
    if sexo in "Mm":
        count_m += 1

    elif sexo in "Ff" and idade < 20:
        count_f += 1

    while sexo not in "FfMm":
        sexo = str(input("Digite F para Feminino e M para masculino: "))

    continuar = str(input("Deseja continuar a cadastrar? [S/N]")).strip().upper()
    if continuar in "Nn":
        break

    while continuar not in "SsNn":
        continuar = str(input("Digite S para Sim e N para Não: "))
        continue

print(f"{count} pessoas tem mais de 18 anos")
print(f"{count_m} homens cadastrados")
print(f"{count_f} mulheres tem mais de 20 anos")
