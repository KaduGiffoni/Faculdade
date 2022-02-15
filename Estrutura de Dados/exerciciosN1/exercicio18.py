# 18 - A empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00 por hora extra.
# Faça um algoritmo para calcular e imprimir o salário bruto e o salário líquido de um determinado
# funcionário. Considere que o salário líquido é igual ao salário bruto descontando-se 10% de
# impostos.

hNormal = 10
hExtra = 15

horaEntrada = int(input("Digite a quantidade de horas normais:"))
horaExtra = int(input("Digite a quantidade de horas extras:"))

salario = (horaExtra * hExtra + horaEntrada * hNormal)
desconto = salario - salario*0.1

print(f'salario bruto: R${salario}\nSalario liquido: R${desconto}')