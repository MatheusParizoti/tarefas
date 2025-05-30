# 12.Classe Lista Encadeada
# Crie uma classe de lista encadeada, com os seguintes métodos:
	# adicionar item no final da lista
	# adicionar item no começo da lista
	# remover item no final da lista
	# remoter item no começo da lista

class Lista_Encadeada():
    def __init__(self):
        self.head = None
        self.tail = None
        self.lista = {}

    def adicionar_final(self,chave,valor):

        novo_no = {"valor": valor, "proximo": None}
        if not self.lista:
            self.lista.update({chave: novo_no})
            self.head = chave
            self.tail = chave
        else:
            #Aqui ele procura o ultimo nó
            #depois o "proximo" dentro desse nó
            #depis coloca o novo nó criado agora
            self.lista[self.tail]["proximo"] = chave
            #Aqui ele vai colocar o nó na lista
            self.lista.update({chave: novo_no})
            #Aqui ele vai definir se esse novo nó vai ser a tail
            self.tail = chave
        return self.lista

        
    def adicionar_inicio(self,chave,valor):
        # Aqui está colocando o antigo head atras do nó que vamos criar
        novo_no = {"valor": valor, "proximo": self.head}
        # Aqui está colocando o nó na lista 
        self.lista.update({chave: novo_no})
        # Aqui verifica se for o unico nó ele vai ser o head e a tail
        if not self.head:
            self.tail = chave
        # Aqui passagem para que esse nó criado vire um head
        self.head = chave
        
        return self.lista
    
    def remover_inicio(self):
        if not self.head:
            return self.lista  # Lista já está vazia
        #Aqui pega o próximo nó
        proximo = self.lista[self.head]["proximo"]  
        #Aqui remove o atual head
        del self.lista[self.head]
        #Aqui mostra que o "proximo" do head vai virar o head
        self.head = proximo  
        return self.lista
    
    def remover_final(self):
        atual = self.head
        # Percorre até o penúltimo nó
        while self.lista[atual]["proximo"] != self.tail:
            # logica para ele conseguir entrar para o nó seguinte
            atual = self.lista[atual]["proximo"]
        
        # Remove o tail
        del self.lista[self.tail]
        # Aqui fala que o "proximo" do penultimo nó é None
        self.lista[atual]["proximo"] = None
        # Aqui tranforma o penultimo nó em tail
        self.tail = atual  

LE = Lista_Encadeada()
print(LE.adicionar_inicio("nó1","lapis"))
print(LE.adicionar_inicio("nó2","caneta"))
print(LE.adicionar_inicio("nó3","lapizera"))
print(LE.adicionar_final("nó0","pincel"))
