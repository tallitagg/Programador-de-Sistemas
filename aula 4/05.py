compra = float(input("Digite o valor da sua compra: "))
pagamento = input("Digite a forma de pagamento (d- cartão de débito ou c- cartão de crédito): ")

if pagamento == "d": 
    print("O valor final da compra é:", compra*0.95)
elif pagamento == "c":
    print("O valor final da compra é o mesmo!")
else : 
    print("Inválido!!!")


