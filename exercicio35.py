area = float(input("Digite a área a ser pintada (em m²): "))
litros_tinta = area / 3
latas_necessarias = int(litros_tinta / 18) + (1 if litros_tinta % 18 != 0 else 0)
preco_total = latas_necessarias * 80
print(f"Quantidade de latas necessárias: {latas_necessarias}")
print(f"Preço total: R$ {preco_total:.2f}")
