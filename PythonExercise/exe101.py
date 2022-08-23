from datetime import date


def voto(idade):
    if idade < 18:
        print(f"NAO VOTA.")
    elif idade > 18 and idade <= 65:
        print(f"VOTO ORBIGATORIO")
    else:
        print(f"VOTO OPCIONAL")


nasc = int(input("Digite seu ano de nascimento: "))

ano_atual = date.today().year
idade_atual = ano_atual - nasc

voto(idade_atual)

# logica do professor:


def voto(ano):
    from datetime import date

    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f"Com {idade} anor: NAO VOTA."
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
        return f"Com {idade} anos: VOTO OBRIGATORIO."


nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))
