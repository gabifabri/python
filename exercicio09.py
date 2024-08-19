def verificar_multiplo_de_5(numero):
  if numero % 5 == 0:
      return "O número é múltiplo de 5."
  else:
      return "O número não é múltiplo de 5."

entrada = int(input("Digite um número inteiro: "))
print(verificar_multiplo_de_5(entrada))