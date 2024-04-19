nome = input("Digite um nome (o nome deve ser maior que 2 caracteres): ")
while len(nome) <= 2 :
    print("O nome dever ter mais que 2 caracteres!")
    nome = input("Digite um nome:")

idade = int(input("Digite sua idade: "))
while idade < 0 and idade > 150:
    print("Coloque uma idade válida!") 
    idade = int(input("Digite sua idade: "))

salario = float(input("Digite seu salário: "))
while salario < 0:
    print("O salário deve ser maior que 0.")
sexo = input("Digite seu sexo ( F para feminino e M para masculino): ")
while sexo != "f" and sexo != "m":
    print("Digite um sexo válido, como descrito a seguir.")
    sexo = input("Digite seu sexo ( F para feminino e M para masculino): ")

civil = input("Digite seu estado civil ( s - solteiro(a) ; c - casado(a) ; v - viuvo(a) ;  d - divorciado (a))")
while civil != "s" and civil != "c" and civil != "v" and civil != "d":
    print("Estado civil não válido, digite novamente.")
    civil = input("Digite seu estado civil ( s - solteiro(a) ; c - casado(a) ; v - viuvo(a) ;  d - divorciado (a)): ")
print("Informações validadas com sucesso!")