# entrada de dados --> lista de tuplas

funcionarios = []
for _ in range(int(input("Quantos funcionários deseja? -> "))):
    nome = input("Nome: ")
    salario = float(input("Salário: "))
    tempo = int(input("Tempo de seriço: "))
    funcionarios.append((nome, salario, tempo))
    
# Função para aumentar o salário
def aumentar_salario(funcionario):
    nome, salario, tempo = funcionario
    aumento = 0.2 if tempo >= 0.5 else 0.1
    novo_salario = salario * (1 + aumento)
    return (nome, novo_salario, salario)

# map para aplicar o aumento de salario para cada um dos funcionários
funcionarios_atualizado = list(map(aumentar_salario, funcionarios))

# impressão dos dados
for nome, novo_salario, salario_antigo in funcionarios_atualizado:
    print(f'Nome: {nome} - Sálario Antigo: R${salario_antigo:.2f} -> Novo Salário: {novo_salario:.2f}')