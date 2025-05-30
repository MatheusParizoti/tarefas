# 15. Crie uma classe Aluno com os atributos privados nome, nota1 e nota2. Implemente um método media() que retorna a média das notas, e use getters/setters para acessar os atributos.

class Aluno():
    def __init__(self, nome, nota1, nota2):
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def media(self):
        return (self.__nota1 + self.__nota2) / 2
    
a = Aluno("Matheus", 10, 8)
print(a.media)

        