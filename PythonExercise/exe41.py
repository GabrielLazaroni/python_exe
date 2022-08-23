from datetime import date

ano_nasc = int(input("digite a idade do atleta: "))

ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade <= 9:
    print("MIRIM")

elif (
    idade <= 14
):  # nao precisamos colocar que é > 9, no primeiro if ja houve uma verificaçao
    print("INFANTIL")

elif idade <= 19:
    print("JUNIOR")

elif idade <= 25:
    print("SENIOR")

else:
    print("MASTER")
