
numero1 = float(input("Digite o primeiro número positivo e maior que zero:"))
numero2 = float(input("Digite o segundo número positivo e maior que zero:"))
if numero1 > 0 and numero2 > 0:

    resultado = numero1 ** numero2
    print(f"Resultado: {resultado}")

else:
    print("Número inválido. Os números devem ser positivos e maiores que zero.")