# 4 - Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias
# de vida ela possui, Considere sempre anos completos, e que um ano possui 365 dias.
# EX: Uma pessoa com 19 anos possul 6935 dias de vida; veja um exemplo de saída:
# MARIA, VOCÊ JÁ VIVEU 6935 DIAS

idade = int(input('Digite sua idade:'))
ano = 365

print(f'Em {idade} anos voce viveu {idade * ano} dias.')