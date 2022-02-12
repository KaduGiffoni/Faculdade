# 10 - Construa um algoritmo para calcular a distância entre dois pontos do plano cartesiano.
# Cada ponto é um par ordenado (x,y).

ponto1 = input('Digite os valores de x e y do primeiro ponto separados por uma virgula:')
ponto2 = input('Digite os valores de x e y do segundo ponto separados por uma virgula:')

x1,y1 = ponto1.split(',')
x1,y1 = float(x1), float(y1)
x2,y2 = ponto2.split(',')
x2,y2 = float(x2), float(y2)

deltaY = y2 - y1
deltaX = x2 - x1

distancia = ((deltaX**2)+(deltaY**2))**0.5

print(f'a distancia entre os dois pontos no plano carteziano é {int(distancia)}')



