from datetime import date

def voto(idade):
    if idade < 18:
        print(f'NAO VOTA.')
    elif idade > 18 and idade <= 65:
        print(f'VOTO ORBIGATORIO')
    else:
        print(f'VOTO OPCIONAL')
        
        
nasc = int(input('Digite seu ano de nascimento: '))

ano_atual = date.today().year
idade_atual = ano_atual - nasc

voto(idade_atual)    
