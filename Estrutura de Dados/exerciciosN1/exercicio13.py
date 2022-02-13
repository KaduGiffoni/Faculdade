# Ler um numero inteiro (assuma ate tres digitos) e imprimir a saida da seguinte forma:
# CENTENA = X
# DEZENA = X
# UNIDADE = X

numero = int(input('Digite um numero:'))

centena = int(numero/100)*100
dezena = numero%100 - numero%10
unidade = numero%10

print(f'Centena: {centena}\ndezena:{dezena}\nunidade:{unidade}')
