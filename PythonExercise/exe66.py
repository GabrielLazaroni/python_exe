soma = count = 0
while True:
    num = int(input('Digite um número [999 para parar o programa]: '))
    if num == 999:
        break #condiçao de parada(tambem chamada de FLAG)
    soma += num
    count +=1
print(f'A soma dos {count} valores digitados é {soma}')