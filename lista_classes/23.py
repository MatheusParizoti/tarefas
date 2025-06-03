# 23. Crie uma classe Animal com método falar(). Crie as subclasses Cachorro e Gato que sobrescrevem esse método com sons específicos.

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return "O animal faz um som."

class Cachorro(Animal):
    def falar(self):
        return f"{self.nome} diz: Au Au!"

class Gato(Animal):
    def falar(self):
        return f"{self.nome} diz: Miau!"

dog = Cachorro("Rex")
cat = Gato("Mimi")

print(dog.falar())
print(cat.falar())
