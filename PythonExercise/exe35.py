reta1 = float(input('primeiro segmento: '))
reta2 = float(input('segundo segmento: '))
reta3 = float(input('terceiro segmento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('os segmentos podem formar um triangulo!')
else: 
    print('os seguimentos nao podem formar um triangulo!')