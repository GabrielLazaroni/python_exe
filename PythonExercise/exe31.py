distancia = int(input("quantos km?"))

if distancia <= 200:
    valor = distancia * 0.50
    print("o valor cobrado será de: {:.2f}".format(valor))
else:
    valor = distancia * 0.45
    print("o valor da passagem é de: {:.2f}".format(valor))
