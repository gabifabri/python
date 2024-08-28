import math


def calcular_raizes(a, b, c):
    if a == 0:
        raise ValueError("O coeficiente 'a' não pode ser zero.")

    delta = b**2 - 4*a*c

    if delta > 0:
        raiz = math.sqrt(delta)
        x1 = (-b + raiz)/ (2 * a)
        x2 = (-b - raiz) / (2 * a)
        return x1, x2
    elif delta == 0:
        x1 = -b / (2 * a)
        return x1,
    else:
        return "Não há raízes reais."
# Exemplo de uso:
a = 1
b = -3
c = 2 

raizes = calcular_raizes(a, b, c)
print("Raízes:", raizes)


