num = count = soma = 0
while num != 999:
    num =  int(input('digite outro valor: '))
    if num != 999:
        soma += num  
        count += 1
print('{} valores foram digitados e a soma dos valores digitados é {}'.format(count, soma))
