n1 = float(input("Digite sua nota 1: ")) #int-> para números inteiros
n2 = float(input("Digite sua nota 2: ")) #int-> para números inteiros
n3 = float(input("Digite sua nota 3 :")) #int-> para números inteiros
n4 = float(input("Digite sua nota 4: ")) #int-> para números inteiros
media = (n1+n2+n3+n4)/4

print("Sua média é:",media)

if media >= 7 :
    print("Você foi aprovado!!")
else:
    print("Você foi reprovado!!")