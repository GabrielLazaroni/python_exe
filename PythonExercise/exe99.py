from time import sleep


def maior(*num):
    count = maior = 0
    print("Analisando valores...")

    for i in num:
        print(f"{i} ", end="", flush=True)
        sleep(0.2)
        if count == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        count += 1

    print()
    print(f"{count} valores foram passados")
    print(f"o maior numero é {maior}")
    print("-" * 25)


maior(1, 8, 19, 3, 6)
maior(1, 8, 25, 7)
maior(5)
maior()
