# somando os valores impares e multiplos de 3 de 1 a 500

soma = 0
contador = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        #soma = soma + i 
        soma += i
        #contador = contador + 1
        contador += 1
print('a soma dos {} valores impares e multiplos de 3 encontrados é {}'.format(contador, soma))

soma = 0 
contador = 0

for i in range(1, 500, 2):
    if i % 3 == 0:
        soma +=1
        contador += 1