from Funcionario import Funcionario

class Estagiario(Funcionario):
    def __init__(self, nome, salario, cargo, bolsaEstagio):
        super().__init__(nome, salario, cargo)
        self.bolsaEstagio = bolsaEstagio
    
    # Override do método calcular_pagamento()
    def calcular_pagamento(self):
        return self.bolsaEstagio