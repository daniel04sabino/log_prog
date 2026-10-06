# Desenvolva um programa que leia os valores de uma matriz 2 × 4 de números
# inteiros. O programa deve contar quantos valores estão abaixo de um limiar, que
# também será informado pelo usuário, estão presentes na estrutura e exibir a
# contagem total, além de imprimir a matriz completa formatada em linhas e colunas.
matriz=[]

for linha in range(0,2):
    numeros=[]
    for numero in range(0,4):
        numero=int(input('Digite um número: '))
        numeros.append(numero)
    matriz.append(numeros)
print(f'linha 1: {matriz[0]}\nlinha2: {matriz[1]}')