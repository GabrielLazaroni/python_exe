dicionario = {}

dicionario["nome"] = str(input("Digite o nome do aluno: ")).strip()
dicionario["media"] = float(input("Digite a média do aluno: "))

print(f'O nome do aluno é {dicionario["nome"]}')
print(f'A média do aluno é {dicionario["media"]}')

if dicionario["media"] >= 6:
    print("APROVADO!")
else:
    print("REPROVADO!")
