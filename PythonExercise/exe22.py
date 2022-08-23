# nesse caso estamos usando o metodo upper() diretamente no print (onde não mudamos diretamente o conteudo da lista, da string)
nome = input("digite seu nome:")
print(nome.upper())
# ja neste caso, estamos atribuindo o metodo upper() na string, mudando a lista, a string. pois listas sao imutaveis
# se colocarmos o metodo sem atribuir a ele uma nova variavel, recebemos um erro dizendo que nao podemos modificar listas.
nome = input("digite seu nome:")
nome_lower = nome.lower()
print(nome_lower)
