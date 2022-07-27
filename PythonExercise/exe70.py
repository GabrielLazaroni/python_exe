count = total = menor = count2 = 0
barato = ' '

while True:
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o valor do produto: '))
    
    count2 += 1
    total += preco
    
    if preco > 1000:
        count += 1
        
    if count2 == 1 or preco < menor:
        menor = preco
        barato = nome
    
    '''continuar = str(input('Você deseja continuar? [S/N] '))
    
    if continuar not in 'SsNn':
        continuar = str(input('Digite S para Sim ou N para Não: '))
        
    if continuar in 'Nn':
        break''' 
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
    
    
print(f'O total gasto foi de R${total:.2f}')
print(f'{count} produtos custam mais de R$1000,00')
print(f'O produto mais barato é {barato} e seu valor é de R${menor:.2f}')