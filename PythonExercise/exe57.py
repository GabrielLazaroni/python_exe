sexo = str(input('digite seu sexo [F/M]: ')).strip().upper()

while sexo not in 'MF':
    sexo = str(input('escolha M para masculino e F para feminino: ')).strip().upper()

print('sexo {} escolhido. dado coletado com sucesso!'.format(sexo))