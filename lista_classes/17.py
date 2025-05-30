# 17. Implemente a classe Produto com atributos privados nome e preco. Crie um método aplicar_desconto(percentual) que modifica o preço, mas sem permitir que ele fique abaixo de zero.

class Produtos():
    def __init__(self):
        self.__nome = None
        self.__preco = 10

    @property
    def nome(self):
       return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def preco(self):
       return self.__preco
    
    @preco.setter
    def preco(self,preco):
        self.__preco = preco
    
    def desconto(self):
        desconto = 10
        aplicar = self.__preco - (self.__preco * desconto / 100)
        return f"O preço atual do produto é {aplicar}"

p = Produtos()
p.preco = 100
print(p.desconto())  # Saída: O preço atual do produto é 90.0


        
        