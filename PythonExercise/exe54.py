from datetime import date

maior = 0
menor = 0

for i in range(1, 8):
    nasc = int(input("Em que ano a {}ª pessoa nasceu? ".format(i)))
    idade = date.today().year - nasc

    if idade >= 21:
        maior += 1

    else:
        menor += 1

print(
    "{} pessoas não atingiram maior idade e {} pessoas já são maiores".format(
        menor, maior
    )
)

"""idade_maior = date.today().year - nasc

if idade_maior > 18:
    print(idade_maior)
    print('maior idade') 
else:
    print('menor idade')"""
