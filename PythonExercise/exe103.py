def ficha(jogador="Desconhecido", gols=0):
    print(f"O {jogador} marcou {gols} gols ")


j = str(input("Digite o nome do jogador: ")).strip()
g = str(input(f"Quantos gols {j} marcou?"))

if g.isnumeric():
    g = int(g)
else:
    gols = 0
if j.strip() == "":
    ficha(gols=g)
else:
    ficha(j, g)
