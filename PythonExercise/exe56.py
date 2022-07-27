soma = 0
idade_maior = 0
nome_homem_velho = ''
qtd_mulher = 0

for i in range(1,5):
    nome = str(input('nome da {} pessoa: '.format(i))).strip().upper()
    idade = int(input('idade: '.format(i)))
    sexo = str(input('sexo [M/F]: '.format(i))).strip().upper()

    soma += idade
    media = soma / 4

    if i == 1 and sexo == 'M':
        idade_maior = idade
        nome_homem_velho = nome

    if sexo == 'M' and idade > idade_maior:
        idade_maior = idade
        nome_homem_velho = nome        

    if sexo == 'F' and idade < 20:
        qtd_mulher += 1



print('o nome do homem mais velho é {}'.format(nome_homem_velho))
print('a media de idade entre as pessoa é de {}'.format(media)) 
print('{} mulheres tem menos de 20 anos'.format(qtd_mulher))

