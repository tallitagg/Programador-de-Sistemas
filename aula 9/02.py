nota = float(input("Digite uma nota de 0 a 10: "))

while  nota < 0 or nota > 10 :
     print("Informe uma nota maior que 0 e menor que 10")
     nota = float(input("Digite uma nota de 0 a 10: "))
print("Nota inserida com sucesso!")