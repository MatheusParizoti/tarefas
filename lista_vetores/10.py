## Enunciado: Crie uma função que encontre e retorne o maior elemento de uma lista.


def maior_elemento(lista):
  maior = 0
  for i in lista:
    if i >= maior:
      maior = i

  return maior

maior_elemento([1000,2011,302,45,5])