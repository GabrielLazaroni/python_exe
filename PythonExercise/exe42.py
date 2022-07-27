reta1 = float(input('primeiro segmento: '))
reta2 = float(input('segundo segmento: '))
reta3 = float(input('terceiro segmento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('os segmentos podem formar um triangulo!')

    if reta1 == reta2 == reta3:
        print('esse é um triangulo Equilatero')     

    elif reta1 != reta2 != reta3 != reta1:
        print('este é um triangulo Escaleno') 
    
    else: 
        print('este é um triangulo Isoceles')  
        
    
else: 
    print('os seguimentos nao podem formar um triangulo!')
