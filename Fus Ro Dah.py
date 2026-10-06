# Fus Ro Dah
# matriz=[6,10,15,7,9,20,30,12,25]
matriz=[]
for i in range (3):
    linha=[]
    for j in range(3):
        numero=int(input('Digite um número entre 1 e 9: '))
        # while numero<1 or numero>9:
            # numero=int(input('Digite um número entre 1 e 9: '))
        
        
        linha.append(numero)
    
    matriz.append(linha)
print(matriz)
maximo=[]

for j in range(0,3):
    for i in range(0,3):
        # numero= matriz[j][i]
        b =max(matriz[j][i])
        maximo.append(b)
    b =max(matriz[j])
    maximo.append(b)
print(maximo)


# skyrin=[]
# # print(f'matriz é {matriz}')
# for j in range(0,len(matriz)):
#     for i in range(0,len(matriz[j])):
#         numero=matriz[j][i]
#     # print(f'Numero {i}')
#         if numero%3 == 0 and numero % 5 == 0:
#         # i='FUS'
#             matriz[j][i]='Dah'
#         elif (numero%5==0):
#         # i='Ro'3
#             matriz[j][i]='Ro'
#         elif (numero %3==0):
#         # i='Dah'
#             matriz[j][i]='Fus'
#         else:
#             matriz[j][i]='Erro pai'


# # for i in range(0,len(matriz)):
# #     print(i)
# print(matriz)