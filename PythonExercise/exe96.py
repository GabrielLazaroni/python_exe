print('Controle de Terrenos')

def area(a, b):
    res = a * b
    print(f'A area de um terreno de {a} x {b} é de {res}m²')

larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))

area(larg, comp)