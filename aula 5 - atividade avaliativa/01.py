sexo = input("Boa noite! Por favor, digite seu sexo (M - Masculino ; F - Feminino): ")
altura = float(input("Agora, digite sua altura: "))

if sexo == "M" :
    if altura >= 1.70 :
        print("Você está apto a se alistar no exército!")
    else :
       print("Infelismente você não está apto a se alistar.")
if sexo == "F" :
    if altura >= 1.60 :
     print("Você está apta a se alistar no exército!")
    else : 
       print("Infelismente, você não está apto a se alistar.")
else :
   print("Inválido.")
  
