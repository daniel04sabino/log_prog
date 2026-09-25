numeros=[]
for i in range(0,3):
    numero= int(input('Digite um número: '))
    numeros.append(numero)

print(f'Os números Foram:\n{numeros} ')

for num in numeros:
    if num<0:
        indice=numeros.index(num)
        # numeros[numeros.index(num)]==0
        # numeros.remove(num)
        # numeros.insert(indice,0)
        indice=numeros.index(num)
    
        numeros.insert(indice,0)

print(f'Os números negativos foram substituido pelo 0 e agora ficaram:\n{numeros}')