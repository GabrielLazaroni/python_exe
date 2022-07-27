print('-=' * 10)
print('sequencia Fibonacci')
print('-=' * 10)
num = int(input('\nDigite um numero para saber sua sequendia Fibonacci: '))
t1 = 0
t2 = 1
print('{} > {}'.format(t1, t2), end='')
count = 3
while count <= num:
    t3 = t1 + t2
    print('> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
print('> FIM')