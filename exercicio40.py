nota = float(input("Informe a nota (entre 0 e 10): "))
while nota < 0 or nota > 10:
    print("Nota inválida! Digite um valor entre 0 e 10.")
    nota = float(input("Informe a nota (entre 0 e 10): "))
print(f"Nota válida: {nota}")
