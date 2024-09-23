cont_par = 0
cont_impar = 0
for i in range(10):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1
print(f'Você digitou {cont_par} números pares e {cont_impar} números ímpares.')

