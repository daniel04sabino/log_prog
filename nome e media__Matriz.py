# Construa um programa onde o usuário digitará o nome e a média de dez
# alunos e o programa escreverá, na tela, o nome de todos com a média acima
# ou igual a seis.

# db=[[]]

lista = []
for i in range(0, 10):
    aluno = input('Digite o nome do aluno: ')
    nota = float(input('Digite sua nota: '))
    while nota<0 or nota>10:
        nota = float(input('Digite sua nota: '))
    lista.append([aluno, nota])





for i in range(len(lista)):
    if lista[i][1] >= 6:
        print(f'Aluno: {lista[i][0]} | Nota: {lista[i][1]}')
    elif lista[i][1] < 6:
        print('Alunos Reprovados:\n')
        print(f'Aluno: {lista[i][0]} | Nota: {lista[i][1]}')
