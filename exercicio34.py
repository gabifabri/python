def calcular_peso_ideal(altura, sexo):
  if sexo == 'H':
      return (72.7 * altura) - 58
  elif sexo == 'M':
      return (62.1 * altura) - 44.7
  else:
      raise ValueError("Sexo inválido. Use 'H' para Homens ou 'M' para Mulheres.")

altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (H para Homens e M para Mulheres): ").strip().upper()

try:
  peso_ideal = calcular_peso_ideal(altura, sexo)
  print(f"O peso ideal é: {peso_ideal:.2f} kg")
except ValueError as e:
  print(e)
