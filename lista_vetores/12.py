## Enunciado: Crie uma função que conte quantas vezes um dado elemento aparece em uma lista.

#Usuário pode escolher que elemento ele quer procurar
def escolherElemento(lista):
  elemtento = int(input('Insira um número para procurar na lista:'))
  var = 0
  for i in lista:
    if i == elemtento:
      var += 1
  return f"quantidade de ocorrência é igual á {var} do elemento {elemtento}"

escolherElemento([1,2,3,4,5,6,7,10,9,10])


#Outra Forma de procurar a ocorrencia do elemento na lista
def contar_ocorrencias(lista):
    # Cria um dicionário para armazenar as ocorrências
    contagem = {}

    # Percorre a lista e conta as ocorrências
    for elemento in lista:
        if elemento in contagem:
            contagem[elemento] += 1
        else:
            contagem[elemento] = 1
    return contagem

# Testando a função
lista = [1, 2, 2, 3, 3, 3, 4, 5, 5]
contar_ocorrencias(lista)
# print(resultado)