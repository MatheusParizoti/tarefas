## Enunciado: Crie uma função que receba uma lista e retorne uma nova lista onde cada
## elemento aparece duas vezes consecutivas.

lista = [1, 2, 3]

def consecutiva(lista):
    nova_lista = []
    for i in lista:
        nova_lista.append(i)
        nova_lista.append(i) 
    return nova_lista

nova_lista = consecutiva(lista)
print(nova_lista)

