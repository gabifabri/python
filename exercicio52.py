n = int(input("Digite um número inteiro: "))
cont_div = 0
print("Números primos entre 1 e", n, ":")
for i in range(2, n + 1):
    primo = True
    for j in range(2, int(i ** 0.5) + 1):
        cont_div += 1
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i, end=" ")
print("\nNúmero de divisões realizadas:", cont_div)