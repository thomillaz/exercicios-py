'''dicionario = {}
dicionario = dict{}'''

dicionario = {'nome': 'Milla', 'idade': 25, 'altura': 1.64}
print(dicionario)
print(dicionario['idade'])

dicionario['programadora'] = True
print(dicionario)

for chave in dicionario:
    print(chave, dicionario[chave])

print('peso' in dicionario)
print('altura' in dicionario)
