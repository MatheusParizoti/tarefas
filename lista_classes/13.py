# 13.Classe Lista Encadeada Dupla
# Crie uma classe de lista encadeada dupla, com os seguintes métodos:
# 	adicionar item no final da lista
# 	adicionar item no começo da lista
# 	remover item no final da lista
# 	remoter item no começo da lista

class Lista_Dupla():
    def __init__(self):
        self.head = None
        self.tail = None
        self.lista = {}

    def adicionar_inicio(self, chave, valor):
        novo_no = {"valor": valor, "proximo": self.head, "anterior": None}
        if not self.head:
            self.tail = chave
        else:
            self.lista[self.head]["anterior"] = chave
        self.lista[chefe := chave] = novo_no
        self.head = chave
        return self.lista

    def adicionar_final(self, chave, valor):
        novo_no = {"valor": valor, "proximo": None, "anterior": self.tail}
        if not self.tail:
            self.head = chave
        else:
            self.lista[self.tail]["proximo"] = chave
        self.lista[chave] = novo_no
        self.tail = chave
        return self.lista

    def remover_inicio(self):
        if not self.head:
            return self.lista
        proximo = self.lista[self.head]["proximo"]
        del self.lista[self.head]
        self.head = proximo
        if self.head:
            self.lista[self.head]["anterior"] = None
        else:
            self.tail = None
        return self.lista

    def remover_final(self):
        if not self.tail:
            return self.lista
        anterior = self.lista[self.tail]["anterior"]
        del self.lista[self.tail]
        self.tail = anterior
        if self.tail:
            self.lista[self.tail]["proximo"] = None
        else:
            self.head = None
        return self.lista
