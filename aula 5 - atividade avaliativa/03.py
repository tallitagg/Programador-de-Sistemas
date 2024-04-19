conversao = input("Digite o tipo de conversão de temperaturas que deseja fazer ( F para fahrenheit e C - para Celcius): ")
temp = float(input("Digite a temperatura: "))

if conversao == "F" :
    print("A temperatura convertida é: ",(temp-32)*5/9,"graus Celsius.")
else : 
    print("A temperatura convertida é: ",(temp*9/5)+32,"graus Fahremheit.")