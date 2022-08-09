dic = {}
dados = []
print('== ANALISE DE JOGADOR ==')
dic['nome'] = str(input('Qual o nome do jogador? ')).strip()
partidas = int(input(f'Quantas partidas {dic["nome"]} jogou?'))

for i in range(0, partidas):
    dados.append(int(input(f' => Quantos gols {dic["nome"]} fez na {i+1}ª partida? ')))
    dic['gols'] = dados[:]
    dic['total'] = sum(dados) 
print('-' * 30)

for k, v in dic.items():
    print(f'A chave {k} tem o valor {v}')
    
print('-' * 30)
print(f'O jogador {dic["nome"]} jogou {partidas} partidas:\n')

for i, v in enumerate(dic['gols']):
    print(f'=>Na {i+1}ª partida, {dic["nome"]} fez {v} gols\n')
print(f'Total de {dic["total"]} gols')

print('-' * 30)
print(dic)

    


    