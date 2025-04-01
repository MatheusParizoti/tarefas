## Enunciado: Crie uma função que insira um elemento em uma lista apenas se ele ainda
## não estiver presente

lista = [1,2,3,4,5,6]

def inserir():
    n1 = int(input("Digite um numero para inserir na lista: "))
    if n1 in lista:
        print("Infelismente esse numero existe dentro da lista :( ")
    else:
        lista.append(n1)

inserir()
print(lista)