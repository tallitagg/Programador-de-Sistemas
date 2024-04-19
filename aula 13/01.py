# matriz
a = [[1,2,3,4], 
     [6,10,13,8],
     [11,26,13,5],
     [15,62,43,64]] 

a[2][2] = 15
for i in range(4): #posso substituir o range(4) por range(len(matriz))
    for j in range(4):
        print(a[i][j])