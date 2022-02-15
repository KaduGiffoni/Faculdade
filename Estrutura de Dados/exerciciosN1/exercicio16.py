# 16 - A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de
# queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo ou
# presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo em
# que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades (em
# quilos) de queijo, presunto e carne necessários para compra. 

hamburguer = int(input('Digite a quantidade de sanduíches:'))

presunto = 50 
queijo = 50 
carne = 100

print(f'com {hamburguer} hamburgueres voce tera que comprar {float((presunto*hamburguer)/1000)}Kg de presunto, {float((queijo*hamburguer)/1000)}Kg e {float((carne*hamburguer)/1000)}Kg de rodelas de hamburguer')

