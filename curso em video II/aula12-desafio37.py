'''
    Escreva um programa que leia um número inteiro
qualquer e peça para o usuário escolher qual será
a base de conversão:

1 - para binário
2 - para octal
3 - para hexadecimal
'''
num = int(input('Digite um número: '))
print('''
Escolha a base de conversão:
1 - binário
2 - octal
3 - hexadecimal
''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{num} em binário é {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} em octal é {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} em decimal é {hex(num)[2:]}')
else:
    print('Opção inválida.')