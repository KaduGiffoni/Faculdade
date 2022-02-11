# 3 - A padaria Holpão vende uma certa quantidade de pães franceses e uma
# quantidade de broas à cada dia, Cada pãozinho custa R$0,12 e a broa custa R$1,50.
# Ao final do dia, o dono quer saber quanto arrecadou com à venda dos pãos e broas
# (juntos), e quanto deve guardar numa conta de poupança (10% do total arrecadado).
# Você foi contratado para fazer os cálculos para o dono. Com base nestes fatos, faça
# “um algorilmo para ler as quantidades de pães e de broas, e depois calcular os dados solicitados.

paozinho = 0.12
broa = 1.50

entPao = float(input('Digite a quantidade de paes vendidos:\n'))
entBroa = float(input('Digite a quantidade de broas vendidos:\n'))

calcPao = entPao * paozinho
calcBroa = entBroa * broa

print(f'voce vendeu R${calcBroa} em broas e R${calcPao} em paozinhos, somando um total de {calcBroa + calcPao}\n voce devera guardar na sua poupanca um total de R${(calcBroa + calcPao)*0.1:.2f}')





