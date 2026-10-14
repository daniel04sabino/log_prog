# Aluno: Daniel Rocha Sabino

# Desenvolva um programa em Python que leia 10 números inteiros e os armazene em um vetor
# original. A partir dessa estrutura, crie duas novas listas independentes: uma lista denominada pares,
# contendo cada número par do vetor original multiplicado por 3, e uma lista denominada ímpares,
# contendo os números ímpares mantidos com seus valores inalterados. Ao final, o programa deve
# exibir o vetor original, os dois novos vetores resultantes e a contagem exata de elementos alocados
# em cada um deles.

#Lista para receber os números e separar os pares do impares
numeros=[]
pares=[]
impares=[]
#contador
contador_impar=0
contador_par=0

#loop parar receber número
for i in range(0,10):
    num=int(input('Digite um número: '))#número digitados pelo usuário
    numeros.append(num)#adicionar na lista numeros
#percorrer pela lista numeros
for numero in numeros:

    if numero%2==0:#Descobrir se é par
        numero = numero*3# multiplicar por 3
        pares.append(numero)# adicionar na lista pares
        contador_par+=1# adicionar +1 no contador par
    else:
        impares.append(numero)# adicionar na lista impares
        contador_impar+=1 # adicionar +1 no contador impar

# mostrar os 3 vetores e a quantidade de elementos
print(f'Vetor original: {numeros} | quantidade de elementos: {len(numeros)}') 
print(f'Pares multiplicado por 3: {pares} | quantidade: {len(pares)}') #Usei len  e deixei o contador no código
print(f'Impares inalterados: {impares} | quantidade: {len(impares)}') #Usei len  e deixei o contador no código
