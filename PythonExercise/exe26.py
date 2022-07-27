
frase = input('digite uma frase: ').upper().strip()
print('a letra A aparece {} vezes na frase'.format(frase.count('A')))
print('a primeira letra A aparece na posiçao {}'.format(frase.find('A')+1))
print('a ultima letra A aparece na posição {}'.format(frase.rfind('A')+1))