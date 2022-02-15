# 21 - A fábrica de refrigerantes Meia-Cola vende seu produto em três formatos: lata de 350 ml,
# garrafa de 600 ml e garrafa de 2 litros. Se um comerciante compra uma determinada quantidade
# de cada formato, faça um algoritmo para calcular quantos litros de refrigerante ele comprou. 

lata = 350
garrafa = 600
garrafa2 = 2000

compraL = int(input('Digite a quantidade de latas de 350ml:'))
compraG = int(input('Digite a quantidade de garrafas de 600ml:'))
compraG2 = int(input('Digite a quantidade de garrafas de 2l:'))

total = (compraL*lata + compraG*garrafa + compraG2*garrafa2)/1000

print(f'De latas de 350 ml voce comprou {(compraL * lata)/1000}L\nDe garratas de 600ml voce comprou {(compraG * garrafa)/1000}L\nDe garratas de 2l voce comprou {(compraG2 * garrafa2)/1000}\nDando um total de {total}L')