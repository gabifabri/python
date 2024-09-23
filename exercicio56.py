num = int(input("Digite um número entre 0 e 99: "))

if num < 0 or num > 99:
    print("Número inválido. Digite um número entre 0 e 99.")
else:
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

    if num < 20:
        print(unidades[num])
    else:
        dezena = num // 10
        unidade = num % 10
        if unidade == 0:
            print(dezenas[dezena])
        else:
            print(dezenas[dezena], "e", unidades[unidade])
