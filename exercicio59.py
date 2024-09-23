# Para o crescimento da população A, a taxa de crescimento é 3% ao ano
# Para o crescimento da população B, a taxa de crescimento é 1.5% ao ano
# As populações do país A e B são:
# A: 80.000 habitantes
# B: 200.000 habitantes
anos = 0
populacaoA = 80000
populacaoB = 200000
while populacaoA <= populacaoB:
  populacaoA += populacaoA * 0.03
  populacaoB += populacaoB * 0.015
  anos += 1
print(f"Serão necessários {anos} anos para que a população do país A ultrapasse a população do país B.")