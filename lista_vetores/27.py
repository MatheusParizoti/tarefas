## Enunciado: Crie uma função que ordene uma lista em ordem crescente
## implementando o algoritmo de Selection Sort, sem usar métodos nativos de
## ordenação.

def selection_sort(vetor):
    n = len(vetor)
    for i in range(n):
        # Encontra o índice do menor elemento no restante do vetor
        menor_idx = i
        for j in range(i+1, n):
            if vetor[j] < vetor[menor_idx]:
                menor_idx = j
        # Troca o elemento na posição i com o menor encontrado
        vetor[i], vetor[menor_idx] = vetor[menor_idx], vetor[i]
    return vetor

# Exemplo de uso
vetor = [8,7,6]
vetor_ordenado = selection_sort(vetor)
print(vetor_ordenado)