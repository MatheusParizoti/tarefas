# 10.Classe Pedido com Itens
# Crie uma classe que represente um pedido contendo vários produtos. Calcule o valor total.

class Produto():
    def __init__(self):
        pass

    def cadastrar(self,pedido):
        p1 = str(input("Qual o nome do Produto ? "))
        p2 = int(input("Qual o preco do Produto ? "))
        p3 = str(input("Qual a descricao do Produto ? "))
        pedido.pedido[p1] = {"preco": p2, "descricao": p3}
        return f" {p1} foi cadastrado com sucesso"

class Pedido():

    def __init__(self):
        self.pedido = {}

    def mostrar(self):
        return f"{self.pedido}"
    
    def total(self):
       total = sum(produto["preco"] for produto in self.pedido.values())
       return f"esse é o valor total do seu pedido: {total}"
    
produto = Produto()
pedido = Pedido()
print(produto.cadastrar(pedido))
print(produto.cadastrar(pedido))
print(pedido.mostrar())
print(pedido.total())


        