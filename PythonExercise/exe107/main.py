import calculos

num = int(input("Digite um valor: R$"))
porc = int(input("Digite a porcentagem: "))
print(f"{porc}% a mais no valor de {num} é {calculos.aumentar(num, porc)}")
print(
    f"Com desconto de {porc}% no valor de {num}, o valor da compra é de {calculos.diminuir(num, porc)}"
)
print(f"o dobro de {num} é {calculos.dobro(num)}")
print(f"A metade de {num} é {calculos.metade(num)}")
