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

limiar= int(input('Digite o número limiar: '))
quant=0
for linha in matriz:
    
    for numero in linha:
        if limiar>numero:
            quant+=1
            
        


print(f'linha 1: {matriz[0]}\nlinha2: {matriz[1]}')
print(60*'-')
# print(f'linha 1: {matriz2[0]}\nlinha2: {matriz2[1]}')
print(f'Quantidade de números menores que {limiar} são: {quant}')