#algoritimo para saber se um numero é primo 

num = int(input('digite um valor para seber se ele é um numero primo: '))
total = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[31m', end=' ')
        total += 1

    else:
        print('\033[m', end=' ')

    print('{}'.format(i), end=' ')

if total == 2:
    print('\n o numero escolhido é primo!')

else:
    print('\n o numero escolhido NAO é primo')