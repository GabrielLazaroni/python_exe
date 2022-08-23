import calculos

num = float(input("Digite um valor: R$"))
porc = int(input("Digite a porcentagem: "))
print(
    f"{porc}% a mais no valor de {calculos.moeda(num)} é {calculos.aumentar(num, porc, True)}"
)
print(
    f"Com desconto de {porc}% no valor de {calculos.moeda(num)}, o valor da compra é de {calculos.diminuir(num, porc, True)}"
)
print(f"o dobro de {calculos.moeda(num)} é {calculos.dobro(num, True)}")
print(f"A metade de {calculos.moeda(num)} é {calculos.metade(num, True)}")
