from math import cos, radians, tan, sin

angulo = (float(input('difite o angulo desejado: ')))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('o seno é {:.2f}, cosseno é {:.2f} e a tangente é {:.2f}'.format(seno, cosseno, tangente))