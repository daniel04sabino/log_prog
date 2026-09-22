
numeros=[]
for i in range(0,10):
    numero= int(input('Digite um número: '))
    numeros.append(numero)
    
print(numeros)
maior_que_dez=[]

for numero in numeros:
    if numero>=10:
         maior_que_dez.append(numero)
print(maior_que_dez)