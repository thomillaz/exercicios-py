'''for variavel in range(5):
    print(variavel)

    vai imprimir de 0 a 4    
'''


'''for variavel in range(1, 6):
    print(variavel)
    
    vai imprimir de 1 a 5
'''

'''for variavel in range(1, 12, 3):
    print(variavel)

    vai imprimir de 1 a 11, de 3 em 3
'''
media = 0 

for i in range(1, 4):
    nota = float(input(f'informe a sua nota {i}: '))
    media += nota

media = media / 3
print('Sua média é: {:.1f}'.format(media))