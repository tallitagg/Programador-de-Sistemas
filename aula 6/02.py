turno = input("Escolha a opção referente ao turno que você trabalha (m - matutino ; v - vespertino ; n - noturno): ")

match turno :
    case "m" :
        print("Bom Dia!")
    case "v" :
        print("Boa Tarde!")
    case "n" :
        print("Boa Noite!")
    case _ :
        print("Opção Inválida.") 