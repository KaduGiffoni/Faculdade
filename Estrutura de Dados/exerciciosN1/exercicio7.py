# 7 - Entrar com o dia e o mês de uma data e informar quantos dias so passaram desde.
# o início do ano. Esqueça a questão dos anos bissextos e considere sempre que um
# mês possui 30 dias.

mes = 30

entmes = int(input("Digite o mes atual:"))
entdia = int(input("Digite o dia atual:"))

print(f'A quantidade de dias totais desde o inicio do ano é de {entmes * mes + entdia} dias:')
