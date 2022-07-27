from datetime import date

'''ano_nascimento = int(input('em qual ano voce nasceu? '))
idade = date.today().year - ano_nascimento
idade_alistar = 18

if idade < idade_alistar:
    tempo_falta = idade_alistar - idade
    print('você ainda nao tem 18 anos. faltam {} anos para voce se alistar.'.format(tempo_falta))

elif idade == idade_alistar:
    print('está na hora de voce se alistar.')

else:
    tempo_atraso = (date.today().year - ano_nascimento) - 18
    print('passou do tempo de voce se alistar. atraso de {} anos'.format(tempo_atraso))'''

sexo = print('''Qual é o seu sexo? 
[1] MASCULINO
[2] FEMINO
''')
opcao = int(input('escolha uma das opçoes: '))

if opcao == 2:
    print('você nao precisa de alistar')

if opcao == 1:
    ano_nascimento = int(input('em qual ano voce nasceu? '))

    if date.today().year - ano_nascimento < 18:
        tempo_falta = 18 - (date.today().year - ano_nascimento)
        print('você ainda nao tem 18 anos. \033[32m faltam {} anos para voce se alistar.'.format(tempo_falta))

    elif date.today().year - ano_nascimento == 18:
        print('\033[31m está na hora de voce se alistar.')

    else:
        tempo_atraso = (date.today().year - ano_nascimento) - 18
        print('\033[32m passou do tempo de voce se alistar. atraso de {} anos'.format(tempo_atraso))

