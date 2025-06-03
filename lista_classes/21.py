# 21. Crie a classe Funcionario com nome e salário. Crie Gerente e Vendedor como subclasses, adicionando atributos específicos. Exiba as informações usando herança.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_info(self):
        return f'Nome: {self.nome}, Salário: R${self.salario:.2f}'

class Gerente(Funcionario):
    def __init__(self, nome, salario, aumento=100):
        super().__init__(nome, salario)
        self.aumento = aumento

    def exibir_info(self):
        return f'{super().exibir_info()}, Bônus Gerente: R${self.aumento:.2f}'

class Vendedor(Funcionario):
    def __init__(self, nome, salario, aumento=10):
        super().__init__(nome, salario)
        self.aumento = aumento

    def exibir_info(self):
        return f'{super().exibir_info()}, Comissão Vendedor: R${self.aumento:.2f}'

g1 = Gerente("Ana", 8000)
v1 = Vendedor("Carlos", 3000)

print(g1.exibir_info())
print(v1.exibir_info())


    
