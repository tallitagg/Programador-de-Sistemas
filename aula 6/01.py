# exemplo da explicação
# match / case = escolha / caso

dia = int(input("Infome o dia: "))

match dia :
    case 1 :
        print("Domingo")
    case 2 : 
        print("Segunda-feira")
    case 3 :
        print("Terça-feira")
    case 4 :
        print("Quarta-feira")
    case 5 : 
        print("quinta-feira")
    case 6 :
        print("Sexta-feira")
    case 7 : 
        print("Sábado")
    case _ :
        print("Opção Inválida.")