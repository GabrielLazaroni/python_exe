lista = []
lista_par = []
lista3_impar = []

while True:
    num = int(input('Digite o valor: '))
    lista.append(num)
    
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista3_impar.append(num)
        
    resposta = str(input('Deseja continuar? [s/n] ')).strip().upper()
    if resposta in 'Nn':
        break
    
print(f'A lista com numeros pares e impares é {lista}')
print(f'A lista com numeros pares é {lista_par}')
print(f'A lista com numeros impares é{lista3_impar}')
print('programa finalizado.')