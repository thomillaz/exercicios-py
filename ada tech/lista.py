notas = [7.9, 9.7, 8.2]

# criando listas
lista = []
lista = list()
lista = [26, 'Milla', 3.2222, False]
lista_de_listas = [10, [1, 2, 3]]

# indexação e slices (fatiamento)
lista = [10, 'Milla', 3.14, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lista[0:3])

# mostrar toda a lista

for elemento in lista:
    print(elemento)


print('Comprimento da lista: ', len(lista))

for i in range(len(lista)):
    print(lista[i])

# métodos de listas
lista = [1, 3, 12, 8, 2]
print('Antes do append: ', lista)

lista.append(3)
print('Depois do append: ', lista)

lista.insert(2, 10)
print('Depois do insert: ', lista)

lista2 = [1, 2, 3]
lista.extend(lista2)
print('Depois do extend: ', lista)

lista.pop()
print('Lista depois do pop: ', lista)
lista.pop(0)
print('Lista depois do pop: ', lista)

lista.remove(3)
print('Depois do remove: ', lista)

print('Quantidade de 2 na lista: ', lista.count(2))

print('Índice do elemento 12: ', lista.index(12))

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

# funções para listas
print(len(lista))
print(sum(lista))

print('Maior elemento da lista: ', max(lista))
print('Menor elemento da lista: ', min(lista))

