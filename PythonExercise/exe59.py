#minha logica:

"""num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('digite o segundo valor: '))
pri = num1
seg = num2
menu = int(input('''qual calculo voce deseja fazer?
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
Escolha uma das opçoes: '''))

while menu == 4:
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('digite o segundo valor: '))
    pri = num1
    seg = num2
    menu = int(input('''qual calculo voce deseja fazer?
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
Escolha uma das opçoes: '''))

while menu == 1:
    res = num1 + num2
    print(f'a soma de {num1} e {num2} é {res}')
    break

while menu == 2:
    res = num1 * num2
    print(f'a multiplicação de {num1} por {num2} é {res}')
    break

while menu == 3:
    if num1 > num2:
        print(f'O numero {num1} é maior que {num2}. O {pri}º valor é maior! ')
    else:
        print(f'O numero {num2} é maior que {num1}. o {seg}º valor é maior') 
    break   

while menu == 5:
    print('Fechando o promograma.')
    break"""

#logica do professor

num1 = int(input('primeiro valor: '))
num2 = int(input('segundo valor: '))
opcao = 0

while opcao != 5:
    print('''
    [1] soma
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')

    opcao = int(input('qual é a sua opçao?'))
    
    if opcao == 1:
        soma = num1 + num2
        print('a soma entre {} e {} é {}'.format(num1, num2, soma))
    
    elif opcao == 2:
        mult = num1 * num2
        print('a multiplicaçao entre {} e {} é {}'.format(num1, num2, mult))

    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
            print('entre {} e {} oe maior valor é {}'.format(num2, num1, maior))

    elif opcao == 4:
        print('informe os numeros novamente: ')
        num1 = int(input('digite o primeiro valor: '))
        num2 = int(input('digite o segundo valor: '))

    elif opcao == 5:
        print('finalizando ...')

    else:
        print('opçao invalida. tente novamente.')

print('fim do programa.')        