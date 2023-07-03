'''
    Refaça o Desafio 35 dos triângulos, acrescentando o
recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: Todos os lados diferentes
'''
r1 = float(input('Comprimento reta 1: '))
r2 = float(input('Comprimento reta 2: '))
r3 = float(input('Comprimento reta 3: '))

print(f'Reta 1: {r1} \nReta 2: {r2} \nReta 3: {r3}')

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas podem formar um triângulo!')
    if r1 == r2 == r3:
        print('Triângulo equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Triângulo isóscele.')
    else:
        print('Triângulo escaleno.')
else:
    print('Essas retas não podem formar um triângulo.')
