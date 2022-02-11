# 6 - O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. Escreva
# um algoritmo que leia o peso do prato montado polo cliento (em quilos) e imprima o.
# valor a pagar. Assuma que a balança já desconto o peso do prato.

kg = 12
prato = 0.3

peso = float(input('digite o peso total da balança:\n'))

print(f'o peso total foi de {peso-prato}, e o valor total a pagar e de R${(peso-prato)*kg:.2f}')