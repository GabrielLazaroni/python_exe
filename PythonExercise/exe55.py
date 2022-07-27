maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('qual o peso da {}ª pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso foi {:.2f}Kg e o menor foi {:.2f}Kg'.format(maior, menor))
    