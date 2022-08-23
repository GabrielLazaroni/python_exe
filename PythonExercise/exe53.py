# algoritimo para saber se um frase ou palavra é palindromo(a palavra é a mesma de tras para frente)

frase = str(input("digite uma frase: ")).strip()
frase2 = frase.replace(" ", "")

for i in frase2.split():
    reverse = frase2[::-1]

if reverse == frase2:
    print("essa palavra é um polindromo")

else:
    print("essa palavra nao é um polindromo")
