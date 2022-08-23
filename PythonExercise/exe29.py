car = int(input("qual a velocidade do carro? "))

if car > 80:
    multa = (car - 80) * 7
    print("velocidade limite ultrapssada! voce foi multado!")
    print("sua multa é de R${}".format(multa))
else:
    print("você está dentro do limite de velocidade!")
