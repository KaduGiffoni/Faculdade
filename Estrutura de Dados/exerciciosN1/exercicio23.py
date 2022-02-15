# 23. Num dia de sol, você deseja medir a altura de um prédio, porém, a trena não é suficientemente
# longa. Assumindo que seja possível medir sua sombra e a do prédio no chão, e que você lembre
# da sua altura, faça um algoritmo para ler os dados necessários e calcular a altura do prédio.

tng45Sol = 1


altura = float(input('Digite a sua altura:'))
sombra1 = float(input('Digite o tamanho da sua sombra:'))
sombra2 = float(input('Digite o tamanho da sombra do predio:'))

calc = (sombra2 * altura)/sombra1

print(f'a altura do predio e {calc} metros')


