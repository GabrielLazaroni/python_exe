lista = []

while True:
    nome = str(input('Digite o nome do aluno: ')).strip()
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    
    resp = str(input('Deseja continuar: [s/n]')).strip().upper()
    if resp in 'N':
        break

print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')

for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
    
while True:
    escolha = int(input('Voce quer mostrar as notas de qual aluno? '))
    
    if escolha == 999:
        break
    if escolha <= len(lista) -1:
        print(f'As notas de {lista[escolha][0]} são {lista[escolha][1]}')




    
     
    