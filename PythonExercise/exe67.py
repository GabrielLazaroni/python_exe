while True:
    num = int(input("Digite um numero para saber sua TABUADA: "))
    if num < 0:
        print("programa fechado")
        break
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
