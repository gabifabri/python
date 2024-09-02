
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (Soma, Subtração, Multiplicao, Divisao): ")
if operacao == "Soma" or operacao == "soma":
    resultado = numero1 + numero2
    print(f"Resultado: {resultado}")

elif operacao == "subtracao" or operacao == "Subtracao":
    resultado = numero1 - numero2
    print(f"Resultado: {resultado}")

elif operacao == "multiplicacao" or operacao == "Multiplicacao":
    resultado = numero1 * numero2
    print(f"Resultado: {resultado}")

elif operacao == "divisao" or operacao == "Divisao":
    resultado = numero1 / numero2
    print(f"Resultado: {resultado}")

else:
    print("Operacao invalida. Por favor, escolha entre Soma, Subtracao, Multiplicacao ou Divisao.")











