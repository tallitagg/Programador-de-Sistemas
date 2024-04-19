lado1 = float(input("Digite a medida do lado 1 do triângulo: "))
lado2 = float(input("Digite a medida do lado 2 do triângulo: "))
lado3 = float(input("Digite a medida do lado 3 do triângulo: "))

if lado1 == lado2 == lado3 :
    print("Esse triângulo é Equilátero!!")
elif lado1 != lado2 != lado3 : 
    print("Esse triângulo é Escaleno!!")
else :
    print ("Esse triângulo é Isósceles!!")