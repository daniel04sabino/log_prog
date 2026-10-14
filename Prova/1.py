# Aluno: Daniel Rocha Sabino

# Construa um programa em Python que solicite 6 números inteiros ao usuário e os armazene em
# uma lista. Em seguida, percorra a lista para calcular a média aritmética de todos os valores
# informados e determinar a quantidade de números pares presentes. Ao final da execução, o
# programa deve exibir a lista completa, o valor da média calculada e o total de elementos pares
# encontrados.


numeros=[] #lista para armazenar os números do usuário
pares=0 #contador dos números pares

#loop para conseguir 6 números
for i in range(0,6):
    num=int(input('Digite um número: ')) #receber o número
    numeros.append(num) #adicionar o número na lista


soma=sum(numeros)#Somar todos os números na lista
media=soma/(len(numeros)) #Descobrir a média

#percorrer na lista
for numero in numeros:
    if numero%2==0: # descobrir se é par
        pares+=1 # adicionar +1 no contador
        
#mostrar na tela
print(f'Lista completa: {numeros} | Media: {media} | Quantidade de números pares: {pares}')