dias_usados = int(input("o carro foi usado durante quantos dias?"))
km_percorridos = float(input("quantos KMs foram percorridos com o carro?"))
preço_dia = dias_usados * 60
preço_km = km_percorridos * 0.15
pago = preço_dia + preço_km
print(
    f"são {preço_dia:.2f} pelos dias usados e {preço_km:.2f} por km rodado. Total de R${pago:.2f}"
)
