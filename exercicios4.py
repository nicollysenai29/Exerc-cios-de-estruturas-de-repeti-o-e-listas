todos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
impar = [ ]
par = [ ]


print(todos)

for valor in todos:
    resto = valor % 2
    if (resto == 0):
        par.append(valor)
    else: 
        impar.append(valor)

print(par)

print(impar)
