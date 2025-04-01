## Enunciado: Crie uma função que combine duas listas e retorne uma única lista com
## todos os elementos.

lista1 = [1,3,5,7,9]
lista2 = [2,4,6,8,10]

lista3 = []

## Jeito feito
def juntar():
    ListaPlus = lista1 + lista2
    print("")
    print("Jeito Feito Porem Certo Tambem")
    print(ListaPlus)

juntar()

## Jeito bonito
def juncao():
    for i in lista1:
        lista3.append(i)
    for _ in lista2:
        lista3.append(_)
    lista3.sort()
    print("")
    print("Jeito Bonitinho")
    print(lista3)

juncao()