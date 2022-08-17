def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.' , ',')


def resumo(preco=0, taxaaumento=10, taxareducao=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(preco)}'.center(30))
    print('-' * 30)
    print(f'O dobro do valor: \t{dobro(preco, True)}')
    print(f'A metade do valor: \t{metade(preco, True)}')
    print(f'Desconto de {taxareducao}%: \t{diminuir(preco, taxareducao, True)}')
    print(f'Aumento de {taxaaumento}%: \t{aumentar(preco, taxaaumento, True)}')
    print('-' * 30)
    