nota = float(input('digite a primeira nota do aluno: '))
nota2 = float(input('digite a segunda nota do aluno: '))
media = (nota + nota2) / 2

if media < 5:
    print('\033[31mREPROVADO')

elif media >= 5  and media < 7:  
    print('\033[35mRECUPERAÇAO')

else:
    print('\033[32mAPROVADO')