# Crie um algoritmo que leia um número
# e mostre o seu dobro, o triplo e raiz quadrada.
num = int(input('Digite um valor: '))
d = num * 2
t = num * 3
r = num ** 0.5 # outra forma: num ** (1/2)
print(' Sobre o número {}: \n o seu dobro é {} \n o seu triplo é {} \n e a sua raíz quadrada é {:.2f}'.format(num, d, t, r))