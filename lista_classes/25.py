# 25. Crie uma função calcular_pagamento(funcionario), que funciona com objetos de Funcionario, Gerente e Estagiario, cada um com sua lógica própria de cálculo.

class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_pagamento(self):
        return self.salario_base

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus=2000):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_pagamento(self):
        return self.salario_base + self.bonus

class Estagiario(Funcionario):
    def __init__(self, nome, salario_base, desconto=500):
        super().__init__(nome, salario_base)
        self.desconto = desconto

    def calcular_pagamento(self):
        return self.salario_base - self.desconto
    


# Aqui decide se vai ser Estagiario ou Gerente Baseado no salario
def criar_funcionario(nome, salario_base):
    if salario_base > 2000:
        return Gerente(nome, salario_base)
    else:
        return Estagiario(nome, salario_base)
    
# Aqui vai mostrar a pessoa e quanto ela vai receber e o cargo dela
def calcular_pagamento(funcionario):
    pagamento = funcionario.calcular_pagamento()
    print(f"{funcionario.nome} vai receber: R${pagamento:.2f} ({type(funcionario).__name__})")



f1 = criar_funcionario("Ana", 2500)
f2 = criar_funcionario("Bruno", 2000)
f3 = criar_funcionario("Carlos", 1800)
f4 = criar_funcionario("Daniela", 3000)

calcular_pagamento(f1)
calcular_pagamento(f2)
calcular_pagamento(f3)
calcular_pagamento(f4)
