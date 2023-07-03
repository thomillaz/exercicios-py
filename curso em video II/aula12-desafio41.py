'''
    A Confederação Nacional de Natação precisa de um
programa que leia o ano de nascimento de um atleta e
mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
'''
from datetime import date

nascimento = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
ano = 2023 - nascimento

if ano <= 9:
    print(f'Idade: {ano} anos. Atleta Mirim.')
elif ano <= 14:
    print(f'Idade: {ano} anos. Atleta Infantil.')
elif ano <= 19:
    print(f'Idade: {ano} anos. Atleta Junior.')
elif ano <= 25:
    print(f'Idade: {ano} anos. Atleta Sênior.')
else:
    print(f'Idade: {ano} anos. Atleta Master.')