expressao = str(input("Digite uma expressão: ")).strip().upper()
lista_p = []

for i in expressao:
    if i == "(":
        lista_p.append("(")
    elif i == ")":
        if len(lista_p) > 0:
            lista_p.pop()
        else:
            lista_p.append(")")
            break

if len(lista_p) == 0:
    print("A expressão está certa!")
else:
    print("A expressão está incorreta!")
