# somando somente os numeros pares de uma aplicacao que lê 6 numeros impares ou pares

s = 0
for i in range(0, 6):
    num = int(input("digite um valor: "))
    if num % 2 == 0:
        s += num
print(s)

s = 0
for i in range(1, 7):
    num = int(input("digite um valor: "))
    if num % 2 == 0:
        s += 1  # soma recebe soma mais 1
print(s)
