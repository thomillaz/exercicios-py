# Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.
valor1 = input('Digite algo: ')
valor2 = input('Digite um número: ')
valor3 = input('Digite mais um valor: ')
valor4 = input('Por último, digite algo: ')
print(' {}: é {}, mas é letra ? {}. \n {}: é {}, mas é número? {}. \n {}: é {}, mas é decimal? {}. \n e o último valor é {} (booleano), mas é alfanumérico? {}.'.format(valor1, type(valor1), valor1.isalpha(), valor2, type(int(valor2)), valor2.isnumeric(), valor3, type(float(valor3)), valor3.isdecimal(), type(bool(valor4)), valor4.isalnum()))