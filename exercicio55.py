def eh_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

texto = input("Digite uma sequência de caracteres: ")

if eh_palindromo(texto):
    print(f'"{texto}" é um palíndromo.')
else:
    print(f'"{texto}" não é um palíndromo.')