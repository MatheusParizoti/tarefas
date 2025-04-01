## Enunciado: Crie uma função que receba uma lista e retorne uma nova lista com os
## elementos duplicados removidos, mantendo a ordem original.

lista = [1,2,9,4,1,5,6,4,2]

def tirar_duplicadas():
    lista_nova = []
    for i in lista:
        if i not in lista_nova:
            lista_nova.append(i)
            
    lista_nova.sort()
    print(lista_nova)

tirar_duplicadas()