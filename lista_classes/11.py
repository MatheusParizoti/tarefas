# 11.Classe Funcionario com Aumento Salarial
# Crie atributos nome e salario. Adicione um método que aplique aumento percentual.

class Funcionario():
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

class Aumento():

    def __init__(self):
        pass

    def salarial(self,funcionario):
        p1 = int(input("Quanto de Aumento voce quer 1-10?"))
        if p1 <= 10:
            transformar = p1 * 10
            print(f"seu aumento é de {transformar}%")
            percentual = funcionario.salario * (transformar / 100)
            conta = funcionario.salario + percentual
            print(f"salario antigo: {funcionario.salario}")
            return f"Parabens {funcionario.nome} seu salarial foi para {conta}"
        

clt = Funcionario("Matheus",1500)
empresa = Aumento()
print(empresa.salarial(clt))

