## Enunciado: Crie uma lista vazia e use append para adicionar os números 5, 3, 8, 6 e 1.
## Imprima a lista resultante.


def exercicio2():
    lista = []

    for i in range(5):
        
        n1 = int(input(f"Coloque o numero: {i+1}: "))
        lista.append(n1)

    print(lista)
    
exercicio2()