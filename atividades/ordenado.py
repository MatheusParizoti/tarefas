# função para inserir elemento no vetor ordenado

vetor1a = [5,2]

def inserir():

    for i in range(2):
        n1 = int(input("Digite um numero para add no vetor 1: "))
        vetor1a.insert(0,n1)
  
    vetor1a.sort()

print(f"Aqui está o vetor ordenado {vetor1a}")

# função para excluir

vetor1b = [1,2,3]

def excluir():  
    del(vetor1b[2]) # escolha a posição que voce deseja apagar dentro do vetor

    # Alternativo
    # valor = int(input("Digite o valor que voce quer excluir: "))

    # if valor in vetor1b:
    #     vetor1b.remove(valor)

print(f"Aqui está o vetor ordenado {vetor1b}")

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


inserir()
excluir()
pesquisar()  

