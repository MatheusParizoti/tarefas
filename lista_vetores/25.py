## Enunciado: Crie uma função que retorne uma lista com os índices em que um
## determinado valor ocorre em uma lista.

lista = [1,2,4,5,4]

NovaLista = []

def indices():
    n1 = int(input("Digite um numero: "))
    for i in range(len(lista)):
        if n1 == lista[i]:
            NovaLista.append(i)
    else:
        print("Esse numero não existe")

indices()
print(NovaLista)