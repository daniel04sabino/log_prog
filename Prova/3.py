# Aluno: Daniel Rocha Sabino

# Construa um programa em Python que receba os dados para preencher uma matriz 3x3 com ok
# números inteiros informados pelo usuário. Após o preenchimento, o sistema deve solicitar um valor
# numérico de corte (limiar). O programa deve varrer a matriz, contabilizar quantos elementos são
# estritamente maiores que esse limiar e gerar uma segunda matriz 3x3 onde todos os valores
# superiores ao limiar sejam substituídos por 0, mantendo os demais inalterados. Ao final, exiba a
# contagem de elementos acima do limiar e a matriz resultante formatada em linhas e colunas.

import copy #importando copy porque apenas matriz2.copy(matriz) fica dando erro

matriz=[]

for j in range(0,3):# loop para receber números e linha para a matriz
    linha=[]#lista para formar uma matriz
    for i in range(0,3):#loop para linha da matriz
        num=int(input('digite um número: '))#armazenar um número
        linha.append(num)#salvar a o numero na linha
    matriz.append(linha)#salvar a coluna na matriz

limiar=int(input('Digite um número limiar: ')) #Definindo o número limiar

matriz2=[] 
matriz2= copy.deepcopy(matriz)#copiar a matriz 1

for linha in matriz2:
    for numero in linha:#percorrer na linha da matriz
        if numero>limiar:#Descobrir se o número é maior q limiar
            posicao=linha.index(numero)#Descobrir a posição do numero dentro da linha
            numero=0 #Defindo 0
            linha[posicao]=numero #Substituir o número antigo por 0
            
        
#mostrar as duas Matriz      
print(f'Matriz1:\nlinha 1: {matriz[0]}\nlinha 2: {matriz[1]}\nlinha 3: {matriz[2]}')
print(60*'-')# apenas para separar elas
print(f'Matriz2:\nlinha 1: {matriz2[0]}\nlinha 2: {matriz2[1]}\nlinha 3: {matriz2[2]}')
