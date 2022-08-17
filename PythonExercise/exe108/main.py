import calculos

num = float(input('Digite um valor: R$'))
porc = int(input('Digite a porcentagem: '))
print(f'{porc}% a mais no valor de {calculos.moeda(num)} é {calculos.moeda(calculos.aumentar(num, porc))}')
print(f'Com desconto de {porc}% no valor de {calculos.moeda(num)}, o valor da compra é de {calculos.moeda(calculos.diminuir(num, porc))}')
print(f'o dobro de {calculos.moeda(num)} é {calculos.moeda(calculos.dobro(num))}')
print(f'A metade de {calculos.moeda(num)} é {calculos.moeda(calculos.metade(num))}')