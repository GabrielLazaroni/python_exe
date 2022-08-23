lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

maior = menor = soma = soma_coluna = 0

for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f"Digite um valor: [{l} : {c}] "))

print("-" * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{lista[l][c]:^5}]", end="")
        if lista[l][c] % 2 == 0:
            soma += lista[l][c]
    print()
print("-" * 30)
print(f"a soma de todos os numero pares digitados é {soma}")

for l in range(0, 3):
    soma_coluna += lista[l][2]
print(f"A soma de todos os valores da 3ª coluna é {soma_coluna}")

"""for i in lista: 
    soma_coluna = lista[0][2] + lista[1][2] + lista[2][2]
print(f'A soma de todos o valores da 3ª coluna é {soma_coluna}')"""

for i in range(0, 3):
    if i == 0:
        maior = lista[1][c]
    elif lista[1][c]:
        maior = lista[1][c]
print(f"O maior valor na segunda linha é {maior}")
