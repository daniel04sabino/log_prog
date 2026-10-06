# #Construa um programa que leia 10 números inteiros, armazene-os em uma lista e,
# em seguida, solicite um número adicional para consulta. O sistema deve verificar e
# exibir se esse valor está presente no vetor e a quantidade exata de vezes que ele se repete.

lista=[]
# positivo=[]
for i in range(0,10):
    lista.append(int(input('Digite um número: ')))

#print(lista)
adicional=int(input('Digite um número extra: '))

posicao=lista.index(adicional)
quant=0
for numero in lista:
    if numero == adicional:
        quant+=1

# print(quant)

# if quant>1:
#     posicao2=lista.index(adicional,posicao,len(lista))
#     print(f'O número foi {adicional} e ele se repete {quant}x.')
#     # print(f'O número foi {adicional} e a sua  posição é: {posicao+1}º e o 2º que ele aparece é na {posicao2+1}º')
# else:
# # positivo.append(posicao)
#     print(f'O número foi {adicional} e a sua  posição é: {posicao+1}º')

print(f'O número foi {adicional} e ele se repete {quant}x.')