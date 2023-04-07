'''
    Faça um programa que leia uma frase
pelo teclado e mostre:

> quantas vezes aparece a letra 'A';
> em que posição ela aparece pela primeira
vez;
> em que posição ela aparece pela última vez.
'''
frase = str(input('Digite uma frase: ').upper().strip())
vezes = frase.count('A')
primeira = frase.find('A')+1
ultima = frase.rfind('A')+1
print(f'A letra A aparece {vezes} vezes.')
print(f'A primeira letra A apareceu na posição {primeira}')
print(f'A última letra A apareceu na posição {ultima}')