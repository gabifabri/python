turno = input("Digite o turno em que você estuda (M-manha, T-tarde, N-noturno): ").strip().upper()


if turno == 'M':
    print("Bom Dia!")
elif turno == 'T':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")