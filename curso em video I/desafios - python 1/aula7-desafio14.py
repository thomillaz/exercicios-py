# Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus
# Fahrenheit.
c = float(input('Digite a temperatura em °C: '))
f = c * 9 / 5 + 32
print('Temperatura {} °C, equivale a {} °F'.format(c, f))
