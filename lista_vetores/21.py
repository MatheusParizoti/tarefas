## Enunciado: Crie uma função que retorne o segundo maior elemento de uma lista.
## (Considere que a lista pode ter duplicatas.)


lista = [5, 2, 8, 1, 5, 3, 6, 8, 4, 7]

def segundo_maior():
    lista.sort(reverse=True)
    print(lista)

    if lista[0] == lista[1]:
        for i in range(len(lista)):
            if lista[i] != lista[0]:
                return lista[i] 
    else:
        return lista[1]  

print(segundo_maior())  
