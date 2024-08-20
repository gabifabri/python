def calcular_novo_salario(salario_atual):
  aumento = salario_atual * 0.25
  novo_salario = salario_atual + aumento
  return novo_salario
salario_atual = float(input("Digite o salário atual do funcionário: "))  

novo_salario = calcular_novo_salario(salario_atual)
print(f"O novo salário do funcionário é: R${novo_salario:.2f}")