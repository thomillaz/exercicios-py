num = int(input('Digite um número: '))
primo = False

for i in range(2, 10):
    print(i)
    if num % num == 0 and num % i != 0:
        primo = True
    else:
        primo = False

print(primo)