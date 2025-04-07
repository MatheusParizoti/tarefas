## Enunciado: Crie uma função que receba uma lista e retorne a soma de todos os seus elementos.

def somar(lista):
  soma = 0
  for i in range(len(lista)):
    soma = soma + lista[i]
  return soma
oi = [1,2,3,4]

somar(oi)