num = int(input('digite um numero inteiro: '))
print('''Como você deseja converter o numero?
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL''')
opcao = int(input('Escolha uma das opçoes: '))

if opcao == 1:
    print('o numero {} convertido para BINARIO é {}'.format(num, bin(num)[2:]))

elif opcao == 2:
    print('o numero {} convertido para OCTAL é {}'.format(num, oct(num)[2:]))

elif opcao == 3:
    print('o numero {} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))

else:
    opcao > 3
    print('digite um numero de 1 a 3 para escolher uma opçao!')
