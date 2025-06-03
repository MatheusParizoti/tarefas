# 19. Crie a classe base Veiculo com atributos marca e modelo, e um método exibir_info(). Crie duas classes filhas Carro e Moto que herdam de Veiculo.

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f'A marca é {self.marca}, o modelo é {self.modelo}'

class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def exibir_info(self):
        return f'{super().exibir_info()}'

class Moto(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def exibir_info(self):
        return f'{super().exibir_info()}'


carro = Carro("Toyota", "Corolla")
print(carro.exibir_info())
print()
moto = Moto("Honda", "CB500")
print(moto.exibir_info())