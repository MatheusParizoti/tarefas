## Enunciado: Crie uma função que encontre e retorne o menor elemento de uma lista

def menor_elemento(lista):
  menor = lista[0]
  for i in lista:
    if i <= menor:
      menor = i

  return menor

menor_elemento([1000,2011,302,45,5])