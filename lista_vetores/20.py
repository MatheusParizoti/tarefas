## Enunciado: Crie uma função que calcule a média dos elementos de uma lista de
## números.

lista = [1,2,3,4,5,6,7,8,9,10]

def media():
    soma = sum(lista)
    qtd = len(lista)
    mediA = soma / qtd
    print(f"Media da Lista Lista : {mediA}")

media()