## Enunciado: Crie uma função que remova a primeira ocorrência de um elemento de uma lista sem utilizar o método remove.


lista = [1,2,3,14,5,2]
n_del = 2
def removerTodos(lista,valor):
  lista2= []
  nd = 0
  for num in lista:
    if num != valor:
      lista2+=[num]
  return lista2

removerTodos(lista,n_del)




#excluindo apenas a primeira ocorrência
def remover(lista,valor):
  for i in range(len(lista)):
    if lista[i] == valor:
      return print(f'Esse é o return do IF {lista[:i]+ lista[i+1:]}')
  return print(f'Esse é o return da fora do for {lista}')

remover(lista,n_del)