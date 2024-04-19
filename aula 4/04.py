turno =  input("Digite o turno em que você estuda (M para matutino, V para vespertino e N para noturno): ")

if turno == "M" :
    print("Bom Dia!")
elif turno == "V" :
    print("Boa Tarde!")
elif turno == "N" :
    print("Boa Noite!")
else : 
    print("Valor Inválido!")