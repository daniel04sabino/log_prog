numeros=[]
organizado=numeros
organizado.sort()
for i in range(0,3):
    numero= int(input('Digite um número: '))
    numeros.append(numero)

organizado=numeros
organizado.sort()
print(f'Essa foi os números que vc digitou:\n{numeros}')
for num in numeros:
    posicao=numeros.index(num)
    print(f'{num} {posicao+1}º')