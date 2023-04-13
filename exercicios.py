letras = ('a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j')
vogais = ('a', 'e', 'i', 'o', 'u')
consoantes = ('b', 'c', 'd', 'f', 'g', 'h', 'j')

for i in letras:
    if i not in vogais:
        print(i)
x = len(consoantes)
print("número de consoantes", x)
