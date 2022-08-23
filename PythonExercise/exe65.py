num = soma = count = maior = menor = 0

while num != "N":
    num = int(input("digite um valor: "))
    count += 1
    soma += num
    media = soma / count
    if count == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    num = str(input("Deseja continuar [S/N]? ")).upper()

print("a media dos valores digitados é {}".format(media))
print("o maior valor digitado foi {}".format(maior))
print("e o menor valor digitado foi {}".format(menor))
