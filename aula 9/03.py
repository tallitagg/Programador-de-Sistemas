nome = input("Digite seu nome: ")
senha = input("Digite uma senha:")

while nome == senha:
    print("A senha deve ser diferente no nome.")
    senha = input("Digite uma senha:")
print("Senha cadastrada com sucesso!")