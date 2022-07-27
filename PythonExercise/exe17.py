from math import hypot

num1 = float(input('digite o valor para o cateto adjacente:'))
num2 = float(input('digite o valor do cateto oposto:'))
hipotenusa = hypot(num1, num2)
print('o valor da hipotenusa é de {:.3f}'.format(hipotenusa))



