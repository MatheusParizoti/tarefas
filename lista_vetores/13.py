## Enunciado: Crie uma função que retorne uma nova lista contendo apenas os números
## pares de uma lista dada.

lista = [1,2,3,4,5,6,7,8,9]
listaNovas = []
def pares():
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            listaNovas.append(lista[i])


pares()

print(listaNovas)