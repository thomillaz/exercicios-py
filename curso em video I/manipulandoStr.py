print('''Lorem ipsum dolor sit amet, consectetur adipiscing elit.Etiam sit amet eleifend libero. Fusce tincidunt feugiat porta.
Pellentesque sit amet viverra elit, sit amet iaculis sapien.
Proin eu ultrices orci, vitae pretium leo.
Fusce venenatis sit amet elit eget ornare.
Sed metus orci, ultrices ut suscipit in, malesuada at nibh.
Cras blandit, dui eget pellentesque pellentesque, ligula ex condimentum urna, quis commodo odio orci non est.\n''')

frase = 'Curso em Vídeo Python'
dividido = frase.split()

print(frase[:15])
print(frase[::2])
print(frase.count('o'))
print(frase.upper().count('C'))
print(frase.replace('Python','Android'))
print('Curso' in frase)
print(frase.lower().find('vídeo'))
print(dividido[0])