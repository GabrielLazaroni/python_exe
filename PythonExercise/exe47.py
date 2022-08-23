# cotando os numeros pares de 1 a 50

# podemos criar esse algoritmo de duas maneiras:
# indicando um calculo matematico para saber quais numero do range sao pares
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# ou mandando o range pular de 2 em 2 numero
# que seria a mesma coisa do calculo matematico, mas usando menos do processador
for i in range(2, 51, 2):
    print(i)
