# 20. Adicione um método ligar() nas classes Carro e Moto que exibe mensagens diferentes. Teste com uma instância de cada classe.

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f'A marca é {self.marca}, o modelo é {self.modelo}'

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def exibir_info(self):
        return f'{super().exibir_info()} e tem {self.portas} portas.'

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def exibir_info(self):
        return f'{super().exibir_info()} com {self.cilindradas} cilindradas.'


carro = Carro("Toyota", "Corolla", 4)
print(carro.exibir_info())
print()
moto = Moto("Honda", "CB500", 500)
print(moto.exibir_info())