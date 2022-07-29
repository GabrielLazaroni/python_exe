lista = [[], []]

for i in range(1, 8):
    num = int(input(f'Digite o {i}º valor: '))
    if num % 2 == 0:
        lista[0].append(num)
        lista[0].sort()
    else:
        lista[1].append(num)
        lista[1].sort()
print(f'A lista de numeros pares: {lista[0]}')
print(f'A lista de numeros impares {lista[1]}')

    