# Construa um programa que receba 8 números inteiros e os guarde em um vetor. Em
# seguida, crie um segundo vetor de mesmo tamanho no qual os números ímpares do
# vetor original sejam multiplicados por 2 e os números pares permaneçam
# inalterados. Ao final, exiba os dois vetores.

lista=[]
for i in range(0,8):
    a=int(input('Digite um número: '))
    lista.append(a)


impares=lista.copy()
posicao=0
for numero in lista:
    if numero%2 !=0:
        posicao=lista.index(numero)
        numero= numero*2
        impares[posicao]=numero


print(f'vc digitou: {lista}\nNova Lista: {impares}')
