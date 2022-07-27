salario = int(input('valor do salario: '))

if salario <= 1250:
    salario_inferior = salario + (salario * 15 /100)
    salario_inferior2 = salario * 15 / 100
    print('seu novo salario é de R${:.2f} e o aumento foi de R${:.2f}'.format(salario_inferior, salario_inferior2))
else:
    salario_superior = salario + (salario * 10 / 100)
    salario_superio2 = salario * 10 / 100
    print('seu novo salario é de R${:.2f} e o aumeto foi de R${:.2f}'.format(salario_superior, salario_superio2))
