valor = float(input('digite o valor da compra: '))
pagamento = int(input('''

MENU:

[1] a vista dinheiro
[2] a vista no cartão
[3] até 2x no cartão
[4] 3x ou mais no cartão

digite uma das opçoes acima: '''))

if pagamento == 1:
    desconto = valor * 10 / 100
    total = valor - (valor * 10 / 100)
    print('você recebeu R${:.2f} de desconto, o valor total com desconto é de: R${:.2f}'.format(desconto, total))

elif pagamento == 2:
    desconto = valor * 5 / 100
    total = valor - (valor * 5 / 100)
    print('você recebeu R${:.2f} de desconto, o valor total com desconto é de R${:.2f}'.format(desconto, total))

elif pagamento == 3:
    print('o valor total da compra é de R${:.2f}'.format(valor))

elif pagamento == 4:
    qtdade_parcelas = int(input('quantas parcelas serão feitas? '))
    juros = valor * 20 / 100
    total = valor + (valor * 20 / 100)
    parcelas = total / qtdade_parcelas
    print('sua compra será parcela em {}x no valor de {:.2f}'.format(qtdade_parcelas, parcelas))
    print('o valor total da compra é de R${:.2f}'.format(total))

else:
    print('\033[31mcondiçao de pagamento não encontrada.')