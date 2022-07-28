valores = []

while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        valores.sort()
        print(valores)
    else:
        print('Valor Dupicado...')
    
    resposta = str(input('Deseja continuar? [s/n]'))
    if resposta in 'Nn':
        break
print(f'o numeros digitados, mostrando em ordem crescente sao: {valores}')
    
        