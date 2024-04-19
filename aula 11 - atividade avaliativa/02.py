manga = int(input("Digite a quantidade de mangás comprados: "))
quant = float(input("Digite o valor pago em cada mangá: "))

for i in range(manga-1):
    quant = float(input("Digite o valor pago em cada mangá: "))
print((manga*quant)/manga)