# -*- coding: utf-8 -*-
a = float(input("Digite o valor de a: "))
if a == 0:
    print("A equação não é do segundo grau.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = (b**2) - 4 * a * c
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        x = (-b + delta ** (1 / 2)) / (2 * a)
        print("A equação possui apenas uma raiz real: ", x)
    else:
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)
        print("A equação possui duas raízes reais: ", x1, " e ", x2)
