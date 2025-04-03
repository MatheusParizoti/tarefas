## Enunciado: Crie uma função que remova o primeiro e o último elemento de uma lista
## e retorne a nova lista.

lista = [1,2,3,4,5]
listaNova = []
ListaFinal = []

print(lista)
def remover_primeiro():
    for i in lista:
        if i != lista[0]:
            listaNova.append(i)
    print(f" lista nova removendo o Primeiro{listaNova}")

remover_primeiro()

def remover_ultimo():
    maior = 0 
    for _ in lista:
        if _ > maior:
            maior = _
            
    for i in lista:
        if i != maior:
            ListaFinal.append(i)
    print(f" lista final removendo o Ultimo Tambem{ListaFinal}")

remover_ultimo()