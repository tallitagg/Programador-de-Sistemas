n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite mais um número: "))

if n1 > n2 and n1 > n3:
    print("O maior número é:",n1)
elif n2>n1 and n2>n3:
    print("O maior número é:",n2)
else:
    print("O maior número é",n3)