## Enunciado: Crie uma função que retorne uma lista com os elementos que são comuns
## a duas listas (sem duplicatas).

lista1 = [1,2,3,4,5]
lista2 = [6,2,7,4,9]
lista3 = []

def comuns():
    for i in lista1:
        for _ in lista2:
            if i == _:
                lista3.append(_)               

comuns()
print(f"Elementos que existem nas 2 listas: {lista3}")
