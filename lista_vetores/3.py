## Enunciado: Crie uma função que receba uma lista e um valor, insira o valor usando append e retorne a lista atualizada.


def funcao_insercao(vetor,valor):
  vetor.append(valor)
  return vetor
num = [1,2,3]
funcao_insercao(num,5)