consersao = int(input("Digite o tipo de conversão que deseja fazer (1 - fahrenheit ; 2 - Celsius): "))
temp = float(input("Digite a temperatura que deseja converter: "))

match consersao :
    case 1 :
        print("A temperatura em Celsius é:",(temp*9/5)+32,"graus.")
    case 2 :
        print("A temperatura em Fahrenheit é:",(temp-32)*5/9,"graus")
    case _ :
        print("Opção Inválida.")