'''
    Refaça o desafio 9, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando laço for.
'''
num = int(input('Digite um número: '))
print('-' * 12)

for i in range (1, 11):
    print(f'{num} X {i:2} = {num*i}')