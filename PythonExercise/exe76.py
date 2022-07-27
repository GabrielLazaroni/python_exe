list = ('Chocolate', 2,
        'Bala', 0.50,
        'Biscoito', 1.50,
        'Chiclete', 1,
        'Pirulito', 0.75)
for i in range(0, len(list)):
    if i % 2 == 0:
        print(f'{list[i]:.<30}', end='')
    else:
        print(f'{list[i]:>.2f}')