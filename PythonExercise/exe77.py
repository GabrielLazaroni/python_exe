list = ('python', 'programar', 'google',
            'computador', 'linguagem', 'string',
            'scripts', 'algoritmo', 'internet')
for i in list:
    print(f'\nna palavra {i.upper()} temos ', end='')
    for letra in i:
        if letra in 'aeiou' :
            print(letra, end=' ')