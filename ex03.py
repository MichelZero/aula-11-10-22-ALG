# 3.	Em linguagem Python, faça um programa que leia 10 inteiros 
# positivos, ignorando não positivos, e imprima sua média.

media = 0
soma = 0
quantidade = 1

while quantidade <= 5:
  valor = int(input(f"informe o valor[{quantidade}]"))
  if valor > 0:
    soma += valor
    quantidade += 1

media = soma / quantidade
# saida
print(f"a média foi: {media}")




