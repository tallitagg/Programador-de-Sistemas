acumulador = 0
num = int(input("Digite um número: "))

while num != 0:
    #acumulador = acumulador + num 
    acumulador += num
    num = int(input("Digite um número: "))
print(acumulador)