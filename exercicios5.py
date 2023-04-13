alunosNotas = [["Nicolly", [8, 8, 9, 10]], ["Nicole", [9, 9 , 10, 10]], ["Mariana", [7, 7, 9, 10]], ["Eloah", [7, 8, 9, 10]]]

def imprimirPrints(alunosNotas):
    print(alunosNotas[0][1][0], alunosNotas[0][1][1], alunosNotas[0][1][2])

def imprimirPop(alunosNotas):
    for aluno in alunosNotas:
        notasTemp = aluno[1]
        notasTemp.pop()
        print(notasTemp)

def imprimirRange(alunosNotas):
    print(alunosNotas[0][1][0:3])

def imprimitForAninhado(alunosNotas):
    for aluno in alunosNotas:
        print(aluno[0])
        for i in range(3):
            print(aluno[1][i])


imprimirPrints(alunosNotas)
imprimirPop(alunosNotas)
imprimirRange(alunosNotas)
imprimitForAninhado(alunosNotas)