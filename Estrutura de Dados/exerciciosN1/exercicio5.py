# 5 - Um motorista deseja colocar no seu tanque X reais de gasolina, Escreva um algoritmo
# para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros
# ele conseguiu colocar no tanque.

vgas = 7.53
pagamento = float(input('Qual o valor do pagamento?\n'))
print(f'voce colocou R${pagamento}, e isso deu o total de {pagamento/vgas:.2f} Litros de gasolina.')