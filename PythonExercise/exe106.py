def ajuda(com):
    help(com)


while True:
    comando = str(input('Funçao ou Biblioteca >> ')).strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)