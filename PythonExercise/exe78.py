valores = []

for i in range(0,5):
    valores.append(int(input('Digite o valor: ')))

print(valores)
print(f'o maior valores digitado foi {max(valores)}')
print(f'o menor valor digitado foi {min(valores)}')

for i, v in enumerate(valores):
    print(f'o indice {i} tem o valor {v}')