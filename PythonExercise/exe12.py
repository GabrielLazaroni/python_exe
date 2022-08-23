valor = float(input("valor do produto:"))
valor_desconto = float(input("valor do desconto:"))
desconto = valor - (valor * valor_desconto / 100)

print(
    f"o valor do produto é de {valor} e com desconto de {valor_desconto} fica {desconto}"
)
