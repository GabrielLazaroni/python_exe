from datetime import date

ano = int(input('digite o ano para seber se é bissexto ou coloque 0 para saber o ano atual '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o ano {ano} é Bissexto')
    
else:
    print(f'o ano {ano} não é Bissexto')