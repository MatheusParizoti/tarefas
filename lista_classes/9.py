# 9.Classe Agenda
# Permita adicionar, listar e buscar contatos com nome e telefone.

class Agenda():
    def __init__(self):
        self.lista = {}

    def adicionar(self):
        p1 = str(input("quem voce deseja adicionar? "))
        p2 = int(input("qual numero voce deseja adicionar? "))
        self.lista[p1] = p2
        print(self.lista)
        return f"{p1} foi adicionado com o número {p2}."
    
    def listar(self):
        return self.lista
    
    def buscar(self):
        p3 = str(input("quem voce deseja procurar? "))
        if p3 in self.lista:
            return f"{p3} foi encontrado no seu celular: número {self.lista[p3]}"
        else:
            return f"não existe {p3} dentro do seu celular" 


celular = Agenda()
print(celular.adicionar())
print(celular.adicionar())
print(celular.listar())
print(celular.buscar())




