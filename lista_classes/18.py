# 18. Crie a classe Temperatura com um atributo privado _celsius e dois métodos públicos get_fahrenheit() e set_fahrenheit(valor) que convertam entre Celsius e Fahrenheit.

class Temperatura():
    def __init__(self,celsius):
        self.__celsius = celsius

    @property
    def fahrenheit(self):
        return self.__celsius
    
    @fahrenheit.setter
    def fahrenheit(self,celsius):
        self.__celsius = celsius

    def converter(self):
        fahrenheit = ((9/5) * self.__celsius ) + 32
        return f"Seus {self.__celsius} agora são {fahrenheit}"
    
temp = Temperatura(20)
print(temp.converter())

