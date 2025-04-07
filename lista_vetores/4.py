## Enunciado: Crie uma função que faça pesquisa linear em uma lista e retorne o índice do elemento se encontrado ou -1 se não estiver presente.

elemento_desejado = int(input("Digite um número: "))
def pesquisa_Linear(elemento_desejado):
  # lista = [1,2,3,4,5,6,4]
  lista = [50,20,3,5,80,90,15]

  for i in lista:
    if elemento_desejado not in lista:
      print('-1')
      break
    if i == elemento_desejado:
      print(lista.index(i))

pesquisa_Linear(elemento_desejado)