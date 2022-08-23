from posixpath import split


name = input("digite sdeu nome:").strip()
print(len(name))

nome = input("digiete seu nome:").strip()
nome_sem_espaço = nome.replace(" ", "")
print(len(nome_sem_espaço))
print(nome_sem_espaço)
