import urllib
import urllib.request

try:
    site = urllib.request.urlopen("https://www.pudim.com.br/")
except urllib.request.URLError:
    print("O site Pudim.com.br não está acessível no momento")
else:
    print("Consegui abrir o Pudim com sucesso!")
