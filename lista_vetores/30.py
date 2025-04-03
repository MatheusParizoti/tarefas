## Enunciado: Crie uma função que receba duas listas de mesmo tamanho (vetores) e
## retorne uma nova lista com a soma elemento a elemento.

lista1 = [1,2,3]
lista2 = [1,2,3]
soma = []
def soma_vetores():
    for i in range(len(lista1)):
        soma.append(lista1[i] + lista2[i])

soma_vetores()
print(soma)