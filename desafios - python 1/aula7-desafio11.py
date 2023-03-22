# Faça um programa que leia a largura e a altura de uma
# parede em metros, calcule sua área e a quantidade de
# tinta necessária para pintá-la, sabendo que cada litro
# de tinta pinta uma área de 2m².
lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = lar * alt
tinta = area/2
print('A área da parede é {:.2f} metros, e necessita de {} litro(s) de tinta para pintá-la.'.format(area, tinta))