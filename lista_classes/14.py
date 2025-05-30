# 14. Criar uma classe ContaBancaria com um atributo saldo privado. Implemente métodos depositar(valor) e sacar(valor). Impedir saque se o valor for maior que o saldo.

class ContaBancaria():
    def __init__(self, senha):
        self.senha = senha
        self.__saldo = 1000  

    def depositar(self):
        p1 = str(input("Qual sua senha ? "))
        if p1 == self.senha:
            p2 = int(input("Qual valor você deseja depositar na sua conta? "))
            self.__saldo += p2
            return f"Sua conta possui R$ {self.__saldo} de saldo"
        else:
            return "Senha incorreta"

    def sacar(self):
        p3 = str(input("Qual sua senha ? "))
        if p3 == self.senha:
            print(f"Saldo atual: R$ {self.__saldo}")
            p4 = int(input("Qual valor você deseja sacar da sua conta? "))
            if p4 <= self.__saldo:
                self.__saldo -= p4
                return f"Sua conta possui R$ {self.__saldo} de saldo"
            else:
                return "Você não possui essa quantia de dinheiro na sua conta"
        else:
            return "Senha incorreta"


Banco = ContaBancaria("a")
print(Banco.depositar())
print()
print(Banco.depositar())
print()
print(Banco.sacar())
print()
print(Banco.depositar())
print()
print(Banco.sacar())
