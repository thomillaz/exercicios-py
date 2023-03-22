# Faça um programa que leia a largura e a altura de uma
# parede em metros, calcule sua área e a quantidade de
# tinta necessária para pintá-la, sabendo que cada litro
# de tinta pinta uma área de 2m².
lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = lar * alt
tinta = area/2
print('A parede tem dimensão {} X {}, a área é de {:.2f} m², e necessita de {:.1f} litro(s) de tinta para pintá-la.'.format(lar, alt, area, tinta))