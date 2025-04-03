## Enunciado: Crie uma função que conte quantos números ímpares existem em uma
## lista.

lista = [1,2,3,4,5,6,7,8,9]
listaNovas = []
def impares():
    for i in range(len(lista)):
        if lista[i] % 2 == 1:
            listaNovas.append(lista[i])


impares()

print(listaNovas)