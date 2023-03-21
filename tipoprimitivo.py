n1 = input('Digite um valor: ')
print(type(n1)) # mostra que n1 é uma string

n2 = int(input('Digite outro valor: '))
print(type(n2))

s = int(n1) + n2
print('A sona entre {} e {} vale {}'.format(int(n1), n2, s))