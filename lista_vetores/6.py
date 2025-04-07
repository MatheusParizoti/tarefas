## Enunciado: Crie uma função que insira um elemento em uma lista ordenada, mantendo a ordem sem usar sort.


lista_ordenada = [10,20,30,40,50]
n_ins = 32

#quando uso o for pelo renge do tamanho eu acesso a POSIÇÃO da minha lista
for i in range(len(lista_ordenada )) :
  if lista_ordenada[i] >= n_ins :
    lista_ordenada.insert(i+1,n_ins)
    break
  if lista_ordenada[i] <= n_ins:
    lista_ordenada.insert(i+1,n_ins)
    break
  if lista_ordenada[i] == n_ins:
    break
  else:
    lista_ordenada.append(n_ins)
    break

print(lista_ordenada)


#quando uso o for direto na lista eu acesso o VALOR que tem na lista
for i in lista_ordenada:
  print(f'esse é o valor {i}')