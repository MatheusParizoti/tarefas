## Enunciado: Crie uma função que insira um elemento em uma lista ordenada,
## mantendo a ordem sem usar sort.
import bisect
lista = [1,2,4,3]

print(lista)

resultado = []
for i in lista:
    bisect.insort(resultado, i)


def inserir():
        n1 = float(input("Digite um numero que voce quer add na lista: "))
        bisect.insort(resultado,n1)

inserir()
print(resultado)