eleitor = int(input("Digite a quantidade de eleitores: "))
print("2101- Tião do Gás ; 2403- Shaolin Matador de Porco ; 1202- Zé da Manga")
tiaodogas = 0
matadordeporco = 0
zedamanga = 0

for i in range(eleitor):
    voto = int(input("Digite o número referente a quem deseja votar: "))
    if voto == 2101:
        tiaodogas += 1
    elif voto == 2403:
        matadordeporco += 1
    elif voto == 1202:
        zedamanga += 1
    else:
        print("O voto foi inválido.")
print("A quantidade de votos do candidato 2101 foi:",tiaodogas)
print("A quantidade de votos do candidato 2403 foi:",matadordeporco)
print("A quantidade de votos do candidato 1202 foi:",zedamanga)
