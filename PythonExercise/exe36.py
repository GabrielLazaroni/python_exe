valor_casa = float(input('digite o valor da casa: '))
salario = float(input('qual o valor do seu salario: '))
parcelas = int(input('em quantas parcelas voce quer dividir a casa? '))

mensalidade = valor_casa /  (parcelas * 12)
salario_porcentagem = salario * 30 / 100

if mensalidade <= salario_porcentagem:
    print('\033[32m o emprestimo foi aprovado!!')

else:
    print('\033[31m o emprestimo foi negado.')
    
