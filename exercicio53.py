eleitores_totais = int(input("Digite o número total de eleitores: "))
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

for i in range(eleitores_totais):
    voto = int(input(f"Eleitor {i + 1}, digite o número do candidato (1, 2 ou 3): "))
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candid