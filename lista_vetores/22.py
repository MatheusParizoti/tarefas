## Enunciado: Crie uma função que retorne o índice do primeiro elemento de uma lista
## que seja maior que um valor dado.

lista = [2,4,6,8,10]

def retornar():
    n1 = int(input("Escolha um numero: "))
    
    for i in range(len(lista)):
        if lista[i] > n1:
            print(i)
            break
        
    else:
        print("Não Existe numero maior que o escolhido")
                
    
            
retornar()
