'''
    A Confederação Nacional de Natação precisa de um
programa que leia o ano de nascimento de um atleta e
mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
'''
nascimento = int(input('Digite seu ano de nascimento: '))
ano = 2023 - nascimento

if ano <= 9:
    print(f'Idade: {ano} anos. Atleta Mirim.')
elif ano > 9 and ano <= 14:
    print(f'Idade: {ano} anos. Atleta Infantil.')
elif ano > 14 and ano <= 19:
    print(f'Idade: {ano} anos. Atleta Junior.')
elif ano == 20:
    print(f'Idade: {ano} anos. Atleta Sênior.')
else:
    print(f'Idade: {ano} anos. Atleta Master.')