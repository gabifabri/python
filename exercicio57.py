suspeito = 0
print("Responda com 'Sim' ou 'Não' para as perguntas a seguir:")
if input("Telefonou para a vítima? ") == "Sim":
    suspeito += 1
if input("Esteve no local do crime? ") == "Sim":
    suspeito += 1
if input("Mora perto da vítima? ") == "Sim":
    suspeito += 1
if input("Devia para a vítima? ") == "Sim":
    suspeito += 1
if input("Já trabalhou com a vítima? ") == "Sim":
    suspeito += 1
if suspeito == 2:
    print("Suspeita")
elif suspeito in range(3, 5):
    print("Cúmplice")
elif suspeito == 5:
    print("Assassino")
else:
    print("Inocente")