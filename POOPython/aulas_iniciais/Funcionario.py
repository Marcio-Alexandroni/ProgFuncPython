class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self._salario = salario  # Um _ indica que o atributo é protegido;
        self.__cargo = cargo     # Dois __ indica que é privado
        
    # Método 'Abstrato' para calcular pagamento    
    def calcular_pagamento(self):  
        pass
    
    # Método get
    def get_salario(self):
        return self._salario
    
    # Método set
    def set_salario(self, salario):
        self._salario = salario
        
    def get_cargo(self):
        return self.__cargo
    
    def set_cargo(self, cargo):
        self.__cargo = cargo
    