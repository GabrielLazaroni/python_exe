# progreçao aritmetica

primeiro = int(input("digite o primeiro termo: "))
razao = int(input("digite a razao: "))
decimo = primeiro + (11 - 1) * razao

for i in range(primeiro, decimo, razao):
    print(i)
