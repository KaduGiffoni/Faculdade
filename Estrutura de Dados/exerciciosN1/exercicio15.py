# 15 - Tres amigos, Carlos, André e Felipe, decidiram rachar igualmente a conta do um
# bar, Faça um algoritmo para ler o valor total da conta e imprimir quanto cada um deve
# pagar, mas faça com que Carlos e André não paguem centavos.
# Ex: uma conta de R$101,53 resulta em R$33,00 para Carlos, R$33,00 para Andre e R$35,53 para Felipe.

conta = float(input('Digite o valor da conta:'))

carlos = int(conta/3)
andre = int(conta/3)
felipe = float(conta/3)

print(f'uma conta de R${conta} resulta em R${carlos} para Carlos, R${andre} para Andre e R${felipe} para Felipe.')