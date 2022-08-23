from time import sleep


def contador(inicio, fim, pula):
    if pula < 0:
        pula *= -1
    if pula == 0:
        pula = 1

    print(f"Iniciando contagem de {inicio} a {fim} pulando de {pula} em {pula}...")
    sleep(0.3)

    count = inicio

    if inicio < fim:
        while count <= fim:
            print(f"{count} ", end="", flush=True)
            sleep(0.3)
            count += pula
        print()
    else:
        while count >= fim:
            print(f"{count} ", end="", flush=True)
            sleep(0.3)
            count -= pula
        print()


contador(1, 10, 1)
contador(10, 0, 2)

print("personalize sua contagem!")

i = int(input("Digite o inicio: "))
f = int(input("Digite até onde voce deseja contar: "))
p = int(input("Pulando de quantos em quantos numeros: "))

contador(i, f, p)
