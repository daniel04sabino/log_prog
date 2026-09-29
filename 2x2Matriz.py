# Construa uma matriz 2X2 e, como saída desse programa, a média e a soma
# dos valores digitados deverão ser calculadas.

# lista = []
# for i in range(0, 2):
#     num1 = int(input('Digite um número: '))
#     num2 = int(input('Digite outro número: '))
#     lista.append([num1, num2])

# soma=sum(lista[0])
# soma2=sum(lista[1])
# media=soma/2
# media2=soma2/2
# print(f'a soma: {soma}\n a média: {media}')
# print('='*40)
# print(f'a soma: {soma2}\n a média: {media2}')


matriz=[]
for i in range(2):
    for j in range(2):
        matriz[i][j]=int(input('Digite um número: '))


soma=0
for linha in matriz:
    for coluna in linha:
        soma+=coluna

for i in range (len(matriz)):
    for j in range(len(matriz[0])):
        soma+= matriz[i][j]
