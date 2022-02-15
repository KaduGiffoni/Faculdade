# 17. Alguns países medem temperaturas em graus Celsius, e outros em graus Fahrenheit. Faça um
# algoritmo para ler uma temperatura Celsius e imprimi-Ia em Fahrenheit (pesquise como fazer este
# tipo de conversão). 

temp = float(input('Digite a temperatura em celcius:'))

conv = (temp * (9/5)) + 32
print(f'em Fahrenheit essa temperatura e: {conv} graus')