numero = int(input("Digite um número: "))
maior = numero
for num in range(4):
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero
print(maior)


