# 2. Em linguagem Python, elabore um programa que leia n valores e 
# mostre a soma de seus quadrados.

# entrada de dados
n = int(input("informe a quantidade de leituras: "))
soma = 0

# processamento
for i in range(n):
  valor = int(input(f"informe um valor[{i+1}]"))
  soma += valor**2 # soma = soma + valor ** 2
  
# saida
print(f"a soma total foi de {soma}")
  




