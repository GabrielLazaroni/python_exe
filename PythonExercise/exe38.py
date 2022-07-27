num1 = int(input('digite o primeiro valor:'))
num2 = int(input('digite o segundo valor: '))

maior = num1
maior2 = num2

if num1 > num2:
    print('o primeiro valor digitado é o maior'.format(maior))

elif num2 > num1:
    print('o segundo valor digitado é o maior'.format(maior2))

else:
    print('os dois valores sao iguais.'.format(num1, num2))