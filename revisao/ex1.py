# Desenvolva um programa que solicite dois números inteiros representando os
# limites de um intervalo [𝐴, 𝐵] (garantindo que 𝐴 ≤ 𝐵). O programa deve iterar sobre
# o intervalo utilizando uma estrutura de repetição e calcular a soma apenas dos
# números ímpares presentes nele, exibindo o resultado final ao usuário.

lista=[]
impar=[]
for i in range(0,6):
    a=int(input('Digite um número: '))
    lista.append(a)

for numero in lista:
    if numero%2 ==0:
        pass
    else:
        impar.append(numero)
soma = sum(impar)
lista.sort()
impar.sort()

print(f'Os números que você digitou:\n{lista}')
print(f'Os números impares:\n{impar}')
print(f'A soma dos impares é: {soma}')
