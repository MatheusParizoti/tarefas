# 7.Classe ContaBancaria
# Crie uma classe com métodos depositar, sacar e extrato.

class Banco():
    def __init__(self,senha):
        self.senha = senha
        self.conta = 0

    def depositar(self):
        p1 = int(input("Qual a sua senha do banco ?"))
        print()
        if self.senha == p1:
            p2 = int(input("Qual a quantia que voce deseja colocar ?"))
            self.conta += p2
            return f"sua conta atualmente possui {self.conta}"
        else:
            return "senha incorreta"
        
    def sacar(self):
        p3 = int(input("Qual a sua senha do banco ?"))
        print()
        if self.senha == p3:
            p4 = int(input("Qual a quantia que voce deseja sacar ?"))
            self.conta -= p4
            return f"sua conta atualmente possui {self.conta}"
        else:
            return "senha incorreta"
        
    def extrato(self):
        return f"sua conta possiu {self.conta}"
        
itau = Banco(1234)
print(itau.depositar())
print(itau.depositar())
print(itau.sacar())

        