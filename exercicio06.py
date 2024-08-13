num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+ ou -): ").strip().lower()

if operacao == "+":
  resultado = num1 + num2
  print(f"O resultado da soma é: {resultado}")
elif operacao == "-":
  resultado = num1 - num2
  print(f"O resultado da subtração é: {resultado}")
else:
  print("Operação inválida. Por favor, escolha '+' ou '-'.")