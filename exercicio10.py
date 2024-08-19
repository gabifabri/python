def tipo_triangulo(lado1, lado2, lado3):
  if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
      if lado1 == lado2 == lado3:
          return "Triângulo Equilátero."
      elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
          return "Triângulo Isósceles."
      else:
          return "Triângulo Escaleno."
  else:
      return "Os lados informados não formam um triângulo."

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))
print(tipo_triangulo(lado1, lado2, lado3))