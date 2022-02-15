# 24 - Um tonel de refresco é feito com 8 partes de água mineral e 2 partes de suco de maracujá.
# Faça um algoritmo para calcular quantos litros de água e de suco são necessários para se fazer X
# litros de refresco (informados pelo usuário). 

suco = float(input('Digite a quantidade de litros de suco:'))

agua = suco*0.8
partSuco = suco*0.2

print(f'serão necessarios {agua} litros de agua e {partSuco} litros de suco')
