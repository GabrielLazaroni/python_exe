name = str(input("digite seu nome completo: ")).strip()
name1 = name.split()
print("seu primeiro nome é {}".format(name1[0]))
print("seu ultimo nome é {}".format(name1[len(name1) - 1]))
