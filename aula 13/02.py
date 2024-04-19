a = [[1,2,3,4], 
     [6,10,13,8],
     [11,26,13,5],
     [15,62,43,64]] 

quant = 0

a[2][2] = 15
for i in range(4): 
    for j in range(4):
        if a[i][j] > 10:
            quant += 1 
print(quant)

