from time import sleep

def contador(inicio, fim, pula):
    print(f'Iniciando contagem de {inicio} a {fim} pulando de {pula} em {pula}...')
    sleep(0.5)
    
    count = inicio
    
    if inicio < fim:
        while count <= fim:
            print(f'{count} ', end='', flush=True)
            sleep(0.5)
            count += pula
        print()
    else:
        while count >= fim:
            print(f'{count} ', end='', flush=True)
            sleep(0.5)
            count -= pula
        print()        
    
contador(1, 10, 1)
contador(10, 0, 2)