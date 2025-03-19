## Enunciado: Crie uma função que remova a primeira ocorrência de um elemento de
## uma lista sem utilizar o método remove.
lista = [1,2,3,4,5]

print(lista)
def remover():
    n2 = int(input("Escolha a posição que deseja deletar: "))
    lista.pop(n2)

remover()

print(lista)
