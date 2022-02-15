# 8 - Faça um algoritmo para ler três notas do um aluno em uma disciplina o Imprimir a sua
# média ponderada (as notas tem posos respectivos de 1, 2 0 3).

notas = input('Digite as tres notas separadas por uma virgula:')
nt1, nt2, nt3 = notas.split(',')
nt1, nt2, nt3 = float(nt1), float(nt2), float(nt3)

media = (nt1 + nt2 + nt3)/ (1+2+3)

print(f'Sua media foi de {media:.2f}')