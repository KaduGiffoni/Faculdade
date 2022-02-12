# 9 - Uma fábrica do camisetas produz os tamanhos pequeno, médio e grande, cada uma
# sendo vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que.
# o usuário forneça a quantidade do camiselas poquenas, médias o grandes referentes
# a uma venda, e a máquina Informe quanto será o valor arrecadado.

p = 10
m = 12
g = 15


qntP = int(input('Digite a quantidade de camisetas pequenas:'))
qntM = int(input('Digite a quantidade de camisetas medias:'))
qntG = int(input('Digite a quantidade de camisetas grandes:'))
total = qntP*p + qntM*m + qntG*g 
print(f'o valor das suas camisas são:\nR${qntP*p} para camisas Pequenas\nR${qntM*m} para camisas medias\nR${qntG*g} para camisas grandes\ndando um todal de R${total}')

