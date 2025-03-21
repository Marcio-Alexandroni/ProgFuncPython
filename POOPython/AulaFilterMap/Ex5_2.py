from random import randint

# entrada de dados --> lista de listas
total_de_listas = int(input("Qual o total de listas? > "))
lista = []

for _ in range(total_de_listas):
    aux = []
    for _ in range(randint(1, 3)):
        aux.append(int(input("Informe o valor --> ")))
    lista.append(aux)
    
# maior lista e seu comprimento   
# somente isto faria o retorno da maior lista dentro de "lista" -> max_lista = max(lista) 

max_lista = max(lista, key=lambda x : len(x))
min_lista = min(lista, key=lambda x : len(x))

print(lista)
print("Lista com comprimento máximo de listas: ", (len(max_lista), max_lista))
print("Lista com comprimento mínimo de listas: ", (len(min_lista), min_lista))
 
 