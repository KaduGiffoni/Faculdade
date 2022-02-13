# 12.Faça um algoritmo para ler o salário do um funcionário e aumentá-lo em 15%. Após
# o aumento, desconte 8% de Impostos. Imprima o salário inicial, o salário com o aumento e o salário final.

salario = float(input( f'Digite o valor do salario do funcionario:'))
aumento = salario + salario * 0.15
desconto = aumento - (aumento*0.08)

print(f'salario inicial: R${salario}\nsalario com aumento: R${aumento:.2f}\nsalario final: R${desconto:.2f}')