## Enunciado: Crie uma função que verifique se um elemento está presente em uma lista,
## retornando True ou False

lista = [1,2,3,4,5]

def verificar():
    pergunta = int(input("Digite um numero dentro da lista: "))
    if pergunta in lista:
        print(f"O numero {pergunta} existe detro da lista 👍")
    else:
        print(f"O numero {pergunta} não existe detro da lista 😢")

verificar()
