# # Desenvolva um programa que solicite dois números inteiros representando os
# # limites de um intervalo [𝐴, 𝐵] (garantindo que 𝐴 ≤ 𝐵). O programa deve iterar sobre
# # o intervalo utilizando uma estrutura de repetição e calcular a soma apenas dos
# # números ímpares presentes nele, exibindo o resultado final ao usuário.

# # lista=[]
# # impar=[]
# # for i in range(0,6):
# #     a=int(input('Digite um número: '))
# #     lista.append(a)

# # for numero in lista:
# #     if numero%2 ==0:
# #         pass
# #     else:
# #         impar.append(numero)
# # soma = sum(impar)
# # lista.sort()
# # impar.sort()

# # print(f'Os números que você digitou:\n{lista}')
# # print(f'Os números impares:\n{impar}')
# # print(f'A soma dos impares é: {soma}')

# lista2=[]
# for i in range(0,3):
#     a=int(input('Digite um número: '))
#     b=int(input('Digite outro número: '))
#     while a<=b:
#         b=int(input('Digite outro número: '))
#     lista2.append([a,b])


# impar2=[]
# tamanho=len(lista2)
# print(tamanho)
# soma=0
# for linha in range(len(lista2)):
#     for numero in range(lis[linha]):
#         if numero%2 != 0:
#             impar2.append(numero)
#             soma += numero
            



# print(soma)
# print(f'A soma dos impares na lista foi {soma}')


def somaimpar(a,b):
    soma=0   
    for i in range(a,b+1):
        if (i%2!=0):
            soma+=i 
    return soma
       
a=int(input('Digite um número: '))
b=int(input('Digite outro número: '))
while a>b:
    b=int(input('Digite outro número: '))
# somaimpar
print(somaimpar(a,b))
    