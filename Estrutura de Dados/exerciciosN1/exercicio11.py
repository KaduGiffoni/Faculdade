# 11. Uma fábrica controla o tempo de trabalho sem acidentes pela quantidade de dias.
# Faça um algoritmo para converter este tempo em anos, meses e dias. Assuma que
# cada mês possui sempre 30 dias.

mes = 30

controle = int(input('Digite a quantidade de dias em que essa empresa nao registra acidentes:'))

meses = controle/mes

if meses > 12:
    