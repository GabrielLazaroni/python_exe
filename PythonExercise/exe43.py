peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))

imc = peso / altura ** 2

if imc < 18.5:
    print('seu imc deu {:.2f} e você está abaixo do peso'.format(imc))

elif imc >= 18.5 and imc < 25:
    print('seu imc é {:.2f} e você tem o peso ideal'.format(imc))

elif imc >= 25 and imc < 30:
    print('seu imc é {:.2f} e você está acima peso'.format(imc))

elif imc >= 30 and imc <= 40:
    print('seu imc é {:.2f} e você está com obesidade'.format(imc))

else:
    print('seu imc é {:.2f} e você está com obesidade morbida'.format(imc))
