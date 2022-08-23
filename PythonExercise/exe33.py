num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))
num3 = int(input("digite o terceiro numero: "))

maior = num1
menor = num1

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

if num2 < menor:
    menor = num2

if num3 < menor:
    menor = num3

print("o maior numero é {} e o menor numero é {}".format(maior, menor))
