numero = int(input("Montar a tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

if inicio > fim:
    print("O valor inicial não pode ser maior que o final.")
else:
    print(f"Tabuada de {numero} começando em {inicio} e terminando em {fim}:")
    for i in range(inicio, fim + 1):
        print(f"{numero} X {i} = {numero * i}")