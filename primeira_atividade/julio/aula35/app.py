import numpy as np

G = np.arange(1, 26).reshape(5, 5)

SL = G.sum(axis=1)
SC = G.sum(axis=0)

print("Matriz G:")
print(G)
print("Somas linhas (SL):")
print(SL)
print("Somas colunas (SC):")
print(SC)
