# 8.Classe Elevador
# A classe deve conter andar_atual, total_andares, capacidade e pessoas. Crie métodos para subir, descer, entrar e sair.

class Elevador():
    def __init__(self, andar_atual,pessoas=0,total_andares=5,capacidade=10):
        self.atual = andar_atual
        self.pessoas = pessoas
        self.andares = total_andares
        self.capacidade = capacidade

    def subir(self):
        if self.atual <= self.andares:
            print(f"atualmente voce está no andar {self.atual}")
            p1 = int(input("qual andar voce deseja subir? "))
            if p1 > p1 or p1 <= self.andares:
                subir = p1 + self.atual
                self.atual = subir - self.atual
                return f"Agora voce está no andar {self.atual}"
            else:
                return "não é possivel subir mais que o limite de andares"
        else:
            return "esse andar não existe dentro do elevador"
        
    def descer(self):
        if self.atual <= self.andares:
            print(f"atualmente voce está no andar {self.atual}")
            p3 = int(input("qual andar voce deseja descer? "))
            if p3 < p3 or p3 <= self.andares:
                descer = p3 - self.atual
                self.atual = descer + self.atual
                return f"Agora voce está no andar {self.atual}"
            else:
                return "não é possivel descer mais que o limite de andares"
        else:
            return "esse andar não existe dentro do elevador"
        
    def entrar(self):
        p4 = int(input("quantas pessoas vão entrar? "))
        if p4 <= self.capacidade:
            self.pessoas += p4
            return f"atualmente tem {self.pessoas} dentro do elevador"
        else:
            return "Esse numero passou o limite maximo do elevador"
        
        
    def sair(self):
        p5 = int(input("quantas pessoas vão sair? "))
        if p5 <= self.pessoas:
            self.pessoas -= p5
            return f"atualmente tem {self.pessoas} dentro do elevador"
        else:
            return "não existe esse numero depessoas dentro do elevador atualmente"


        
comum = Elevador(0)
print(comum.entrar())
print(comum.subir())
print(comum.sair())
print(comum.descer())
print(comum.sair())
print(comum.descer())

        