import concurrent.futures
import random
import time
import math


def gerar_elementos(n):
    return [random.randint(2,100) for _ in range(n)]

def gerar_fator(lista):
    primo = 2
    fator = []
    for valor in lista:
        aux = []
        # Usando a raiz quadrada do valor porque é o mais eficiente para descobrir os numeros primos
        while primo <= math.sqrt(valor):
            if valor % primo == 0:
                fator.append(primo)
                valor //= primo # valor = valor // primo
            else:
                primo += 1
        fator.append((valor, aux))
    return fator


def main():
    num_elementos = 5
    lista = gerar_elementos(num_elementos)    
    inicio = time.time()
    # Execução em Paralelo
    with concurrent.futures.ProcessPoolExecutor() as executor:
        fator = list(executor.map(gerar_fator, lista))
    
    fim = time.time()
    
    for elemento in fator:
        numero, lista = elemento
        print(f'{numero} - {lista}')
        print(f'Tempo = {fim - inicio}')
        
        
 

# Função Principal
if __name__ == '__main__':
    main()