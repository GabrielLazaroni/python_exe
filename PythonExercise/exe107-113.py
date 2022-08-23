from typing import Type


def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mErro! Digite um valor numerico inteiro.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mUsuario preferiu nao digitar esse numero\033[m")
            return 0
        else:
            return n


def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mErro! Digite um valor que seja real.\033[m")
        except (KeyboardInterrupt):
            print("\n\033[31mO usuario preferiu nao digitar esse numero\033[m")
            return 0
        else:
            return n


num = leia_int("Digite um valor inteiro: ")
num1 = leia_float("Digite um valor real: ")
print(f"O valor inteiro digitado foi {num} e o valor real foi {num1}")

# msg2 = leia_float('Digite um valor Float: ')
