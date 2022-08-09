from datetime import datetime

dicionario = {}

dicionario['nome'] = str(input('Digite seu nome: ')).strip()
nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = datetime.now().year
dicionario['idade'] = ano_atual - nascimento
dicionario['ctps'] = str(input('Possui carteira de trabalho? [S/N]')).strip().upper()

if dicionario['ctps'] == 'S':
    dicionario['contratacao'] = int(input('Digite o ano de contratação: '))
    dicionario['salario'] = float(input('Digite o salário: '))
    dicionario['aposentadoria'] = (dicionario['contratacao'] - nascimento) + 35
            #logica do professor:  dicionario['idade'] + ((dicionario['contratacao'] + 35) - datetime.now().year)
    
    for k, v in dicionario.items():
        print(f'o valor de {k} é {v}')
           
else:
    for k, v in dicionario.items():
        print(f'O valor de {k} é {v}')        
