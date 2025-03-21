from Gerente import Gerente
from Estagiario import Estagiario

gerente = Gerente("Jonas", 3000, "gerente", 1500)
print(gerente.calcular_pagamento())

estagiario = Estagiario("Leonardo", 0, "estagiario", 100)
print(estagiario.calcular_pagamento())