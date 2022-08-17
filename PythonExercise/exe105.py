def notas(*num, sit=False):
    """
    -> funcao que analisa notas e situaçao de alunos
    :param n : recebe quantas notas forem necessarias
    :param sit: é opcional, recebe False como padrao, True se quiser adicionar a situaçao no dicionario no output
    :return : retorna um dicionario com informaçoes sobre os alunos
    """
    
    r = {}
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num) / len(num) 
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >=5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp) 
help(notas)