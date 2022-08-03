lista = [[], []]

for i in range(1, 8):
    num = int(input(f'Digite o {i}º valor: '))
    if num % 2 == 0:
        lista[0].append(num)
        lista[0].sort()
        print('Valor adicionado na lista de numero PARES...')
        
    else:
        lista[1].append(num) 
        lista[1 ].sort()
        print('Valor adicionado na lista de numero IMPARES...')
        
print(f'a lista de numeros pares tem os valores: {lista[0]}') 
print(f'a lista de numeros impares tem os valores: {lista[1]}') 
                                               