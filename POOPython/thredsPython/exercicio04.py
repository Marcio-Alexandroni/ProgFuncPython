import concurrent.futures
import random
import time
import math


def gerar_elementos(n):
    return [random.randint(2,100) for _ in range(n)]

def gerar_fator(n):
    primo = 2
    fator = []
    while primo <= math.sqrt(n):
        if n % primo == 0:
            fator.append(primo)
            n //= primo
        else:
            primo += 1
    return fator

def fatorar(n):
    return(n, gerar_fator(n))
    

# Função Principal
def main():
    num_elementos = 5
    lista = gerar_elementos(num_elementos)    
    inicio = time.time()
    print(lista)
    
    # Execução em Paralelo
    with concurrent.futures.ProcessPoolExecutor() as executor:
        fator = list(executor.map(fatorar, lista))
    
    fim = time.time()
    
    for elemento in fator:
        numero, lista = elemento
        print(f'{numero} - {lista}')
        print(f'Tempo = {fim - inicio}')
        
        
 

# Função Principal
if __name__ == '__main__':
    main()