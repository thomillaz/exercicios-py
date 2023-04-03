# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.
valor = float(input('Digite um valor: '))
cent = valor * 100
mili = valor * 1000
print(' O valor {} metros, equivale a \n {:.0f} centímetros \n {:.0f} milímetros'.format(valor, cent, mili))