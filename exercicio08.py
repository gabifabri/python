def verificar_letra(letra):
  letra = letra.lower()
  vogais = 'aeiou'
    
  if letra in vogais:
      return "A letra é uma vogal."
  elif letra.isalpha() and len(letra) == 1:
      return "A letra é uma consoante."
  else:
      return "Entrada inválida."
entrada = input("Digite uma letra: ")
print(verificar_letra(entrada))