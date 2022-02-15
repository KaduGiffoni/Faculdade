# 22. Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu
# poupar. Faça um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor total
# economizado, em reais. Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda
# moedas de 1 real. Não havendo moeda de um tipo, a quantidade respectiva é zero. 


cofre = input('Digite a quantidade de moedas de 1, 5, 10, 25, 50 e 1 real, nessa ordem e separado por virgula:')
qntmoeda1, qntmoeda5, qntmoeda10, qntmoeda25, qntmoeda50, qntmoeda100 = cofre.split(',')
qntmoeda1, qntmoeda5, qntmoeda10, qntmoeda25, qntmoeda50, qntmoeda100 = int(qntmoeda1), int(qntmoeda5), int(qntmoeda10), int(qntmoeda25), int(qntmoeda50), int(qntmoeda100) 

valmoeda1, valmoeda5, valmoeda10, valmoeda25, valmoeda50, valmoeda100 = qntmoeda1 *1, qntmoeda5 *5, qntmoeda10 *10, qntmoeda25*25, qntmoeda50*50, qntmoeda100*100
total = (valmoeda1 + valmoeda5 + valmoeda25 + valmoeda50 + valmoeda100)/100

print(f'a quantidade total e R${total}')