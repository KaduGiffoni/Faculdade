# 11 - Uma fábrica controla o tempo de trabalho sem acidentes pela quantidade de dias.
# Faça um algoritmo para converter este tempo em anos, meses e dias. Assuma que
# cada mês possui sempre 30 dias.

mes = 30

controle = int(input('Digite a quantidade de dias em que essa empresa nao registra acidentes:'))

calcmes = controle / 30
calcano = calcmes / 12

if controle < 30:
    print(f'sua empresa esta a {controle} dias sem acidentes')

if controle >=31 and controle <= 360 and controle%30 == 0:
    print(f'Sua empresa esta a {int(calcmes)} meses sem acidentes')

if controle >=31 and controle <= 360 and controle%30 != 0:
    print(f'Sua empresa esta a {int(calcmes)} meses e {controle%30} dias sem acidentes')

if controle > (360) and calcano%12 == 0:
    print(f'Sua empresa esta a {int(calcano)/12} sem acidentes')

if controle > (360) and calcano%12 != 0:
    if int(calcano) == 1:
        if int(calcmes%12) ==1:
            print(f'Sua empresa esta a {int(calcano)} ano, {int(calcmes%12)} mes e {controle%30} dias sem acidentes')
        else:
            print(f'Sua empresa esta a {int(calcano)} ano, {int(calcmes%12)} meses e {controle%30} dias sem acidentes')
    else:
        if int(calcmes%12) ==1:
            print(f'Sua empresa esta a {int(calcano)} anos, {int(calcmes%12)} mes e {controle%30} dias sem acidentes')
        else:
            print(f'Sua empresa esta a {int(calcano)} anos, {int(calcmes%12)} meses e {controle%30} dias sem acidentes')
        
      