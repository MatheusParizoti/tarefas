# 24. Crie uma função fazer_som(animal) que recebe um objeto e chama animal.falar(). Teste com Cachorro, Gato, Passaro, todos herdando de Animal com método sobrescrito falar().

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

class Passaro(Animal):
    def falar(self):
        return f"{self.nome} diz: Piu Piu!"

def fazer_som(animal):
    print(animal.falar())


dog = Cachorro("Rex")
cat = Gato("Mimi")
bird = Passaro("PiuPiu")

fazer_som(dog)   
fazer_som(cat)   
fazer_som(bird)