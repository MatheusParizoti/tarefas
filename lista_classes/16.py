# 16. Modifique a classe ContaBancaria do exercício 1 para que, ao tentar sacar um valor inválido, uma mensagem de erro seja exibida usando encapsulamento para proteger os dados.
class ContaBancaria():
    def __init__(self, senha):
        self.senha = senha
        self.__saldo = 1000  # saldo privado

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    def depositar(self):
        p1 = str(input("Qual sua senha? "))
        if p1 == self.senha:
            p2 = int(input("Qual valor você deseja depositar na sua conta? "))
            self.__saldo += p2  # usando o setter internamente
            return f"Sua conta possui R$ {self.__saldo} de saldo"  # usando o getter
        else:
            return "Senha incorreta"

    def sacar(self):
        p3 = str(input("Qual sua senha? "))
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
