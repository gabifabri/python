valor_deposito = float(input("Digite o valor do depósito: "))
taxa_juros = float(input("Digite a taxa de juros (em %): "))

rendimento = valor_deposito * (taxa_juros / 100)

valor_total = valor_deposito + rendimento

print(f"Rendimento: R${rendimento:.2f}")
print(f"Valor total após o rendimento: R${valor_total:.2f}")