numeros = []
for num in range(1, 5):
    numeros.append(int(input("Digite o maior numero: ")))

maiorNumero = numeros[0]

cont = 1
while cont < len(numeros):
    if numeros[cont] > maiorNumero:
        maiorNumero = numeros[cont]
    cont = cont + 1
        
print ("O maior numero" + str (maiorNumero))