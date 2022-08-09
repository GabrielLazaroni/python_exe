
dic = {}
pessoas = []
mulheres = []
soma = 0

while True:
    dic.clear()
    dic['nome'] = str(input('Nome: ')).strip()
    
    while True:
        dic['sexo'] = str(input('Sexo: [F/M]')).strip().upper()
        if dic['sexo'] in 'MF':
            break
        print('Digite F para FEMININO e M para MASCULINO.')

    dic['idade'] = int(input('Idade: '))
  
    soma += dic['idade']
    pessoas.append(dic.copy())
    media = soma / len(pessoas)
    
    while True:
        resp = str(input('Deseja Continuar? [S/N]')).strip().upper()
        if resp in 'SN':
            break
        print('Digite S para SIM e N para NÂO.')
    if resp == 'N':
        break
        
print(f'{len(pessoas)} pessoas foram cadastradas')
print(f'A media de idade entre as pessoas cadastradas é de {media}')

for i in pessoas:
    if i['sexo'] == 'F':
        print(f'{i["nome"]} ', end='')
print()

for i in pessoas:
    if i['idade'] >= media:
        print('     ')
        for k, v in i.items():
            print(f'{k} = {v}; ')
        print()
    
    