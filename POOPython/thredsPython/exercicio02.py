import concurrent.futures
import random
import time

# geração de um número
def gerar_hash(n):
    return [random.randint(0,1_000_000) for _ in range(n)]

# função para gerar pares de hash --> gerar o par de tuplas
def gerar_par(par):
    par = []
    for i in range(len(hash)):
        for j in range(i+1, len(hash)):
            par.append((hash[i], hash[j]))
    return par
    
# função para comparar um par (tupla) de Hash
def comparar(par):
    h1,h2 = par
    time.sleep(0.01)
    return (h1, h2, abs(h1 - h2) < 5000)

# Programa Principal
def main():
    num_imagens = 20
    hash = gerar_hash(num_imagens)
    par = gerar_par(hash)

    similar = []
    with concurrent.futures.ProcessPoolExecutor as executor:
        resultados = executor.map(comparar, par)
        
    for resultado in resultados:
        h1, h2, similar = resultado
        if similar:
            print(f'{h1} - {h2}')
        
if __name__ == "__main__":
    main()