## Enunciado: Crie uma função que faça pesquisa linear em uma lista e retorne o índice
## do elemento se encontrado ou -1 se não estiver presente.

lista = [1,2,3,4,5,6,7,8]

print(lista)
def exercicio4():
    n1= int(input("Digite o numero: "))
    
    for i in lista:
        if n1 == i:
            print(f"o numero {n1} existe ")
            return 

    print("O número -1 não foi encontrado no vetor.")

exercicio4()