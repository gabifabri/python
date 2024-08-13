materia = input("Digite o nome da materia: ")

notas = []
for i in range(1, 5):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)
media = sum(notas) / len(notas)
if media >= 7:
    condicao = "Aprovado"
else:
    condicao = "Reprovado"

print(f"\nmateria: {materia}")
print(f"Média: {media:.2f}")
print(f"Condição: {condicao}")
