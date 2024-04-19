n1 = float(input("Digite sua nota 1: "))
n2 = float(input("Digite sua nota 2: ")) 
n3 = float(input("Digite sua nota 3 :")) 
n4 = float(input("Digite sua nota 4: ")) 
media = (n1+n2+n3+n4)/4

print("Sua média é:",media)

if media >= 7:
    print("Aluno aprovado!")
elif media >= 5:
    print("Aluno foi para a recuperação!")
else:
    print("Aluno reprovado!")
 