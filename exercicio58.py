# Ler a quantidade de litros
litros = float(input("Digite a quantidade de litros: "))

# Ler o tipo de combustível
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

# Calcular o valor a ser pago
if tipo == "A":
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    valor = litros * 3.90 * (1 - desconto)
elif tipo == "G":
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    valor = litros * 5.50 * (1 - desconto)
else:
    print("Tipo de combustível inválido.")
    valor = 0

# Imprimir o valor a ser pago
print(f"O valor a ser pago é: R$ {valor:.2f}")