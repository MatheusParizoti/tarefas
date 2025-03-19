# função para inserir elemento no vetor não ordenado

vetor2 = [5,2]

def inserir():

    for i in range(3):
        n2 = int(input("Digite um numero para add no vetor 1: "))
        vetor2.insert(0,n2)  
    
inserir()

print(f"Aqui está o vetor não ordenado {vetor2}")

## função para excluir

vetor2b = [1,2,3]


print(f"Aqui está o vetor {vetor2b}")
def excluir():  
    del(vetor2b[1]) # escolha a posição que voce deseja apagar dentro do vetor

excluir()

print(f"Aqui está o vetor não ordenado {vetor2b}")


## função para pesquisar

vetor1c = [1, 5, 3]

def pesquisar():
    print(vetor1c)
    pergunta = int(input("Digite o numero que voce quer procurar: "))

    for i in vetor1c:
        if pergunta == i:
            print(f"Aqui está o numero que voce pesquisou {pergunta}")
            return 

    print(f"O número {pergunta} não foi encontrado no vetor.")

pesquisar()