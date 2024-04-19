# um colchete pra linha, um pra coluna e outro pra profundidade
a = [
    [[1,2],[3,4]],
    [[10,20],[30,40]]
]
# pode ser usado range(2) em todos os loops das posições da matriz (i,j,k) 
for i in range(len(a)): # len(): retorna a quantidade de elementos na linha da matriz
    for j in range(len(a[i])):# retorna a quantidade de elementos da coluna da matriz
        for k in range(len(a[i][j])): # retorna a quantidade de elementos na profundidade da matriz
            print(a[i][j][k]) # lê cada uma das dimensões da matriz
# são usados 3 for, um para cada dimensão da matriz

