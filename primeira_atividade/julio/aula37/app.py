G = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]  

print("Gabarito da Loteria Esportiva (G):")
print(G)

colunas = {1: "Coluna 1", 2: "Coluna do Meio", 3: "Coluna Dois"}

interpreted_G = [colunas[g] for g in G]

print("\nInterpretação do gabarito:")
print(interpreted_G)
