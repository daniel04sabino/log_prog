# Desenvolva um programa que solicite o preenchimento de uma matriz 3 × 3 com
# números inteiros e, em seguida, peça ao usuário um valor numérico constante
# (escalar). Utilizando laços de repetição aninhados, o programa deve multiplicar cada
# elemento da matriz original por esse valor escalar e exibir a matriz resultante
# formatada em linhas e colunas.
matriz=[]  #3x3
for coluna in range(0,3):
    coluna=[]
    for linha in range(0,3):
        numero=int(input('Digite um número: '))
        coluna.append(numero)
    matriz.append(coluna)

escalar=int(input('digite o número para escalar na matriz: '))
matriz2=[]
posicao=0
for linha in matriz:
    coluna=[]
    
    for numero in linha:
        posicao=linha.index(numero)
        numero=numero*escalar
        coluna.append(numero)
    matriz2.append(coluna)


     
    # matriz2.append(coluna)
print(f'Matriz1:\nlinha 1: {matriz[0]}\nlinha2: {matriz[1]}')
print(60*'-')
print(f'Matriz2:\nlinha 1: {matriz2[0]}\nlinha2: {matriz2[1]}')
