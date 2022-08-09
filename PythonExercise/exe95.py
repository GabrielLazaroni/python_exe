time = []
dic = {}
dados = []
print('== ANALISE DE JOGADOR ==')

while True:
    dic.clear()
    dic['nome'] = str(input('Qual o nome do jogador? ')).strip()
    partidas = int(input(f'Quantas partidas {dic["nome"]} jogou?'))
    dados.clear()
    
    for i in range(0, partidas):
        dados.append(int(input(f' => Quantos gols {dic["nome"]} fez na {i+1}ª partida? ')))
    dic['gols'] = dados[:]
    dic['total'] = sum(dados)
    time.append(dic.copy())
    
    while True:
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()
        if resp in 'SN':
            break
        print('Responda apenas com S para sim ou N para não.')
    if resp in 'N':
        break
            

print('-' * 30)
print(f'O jogador {dic["nome"]} jogou {partidas} partidas:\n')

for i, v in enumerate(dic['gols']):
    print(f'=>Na {i+1}ª partida, {dic["nome"]} fez {v} gols\n')
print(f'Total de {dic["total"]} gols')