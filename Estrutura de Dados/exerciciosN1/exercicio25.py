# 25 - Calcule o volume de uma caixa d'água cilíndrica.

raio = float(input('Digite o raio da caixa de agua:'))
altura = float(input('Digite a altura da caixa de agua:')) 

volume = 3.14 * raio**2 *altura

print(f'O volume da caixa de agua é {volume:.2f} cm³')
