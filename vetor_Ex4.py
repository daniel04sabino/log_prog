numeros=[]
inverso=numeros
for i in range(0,3):
    numero= int(input('Digite um número: '))
    numeros.append(numero)

print(f'Essa foi os números que vc digitou:\n{numeros}')
inverso.reverse()
print(f'Essa foi inverso dos números que vc digitou:\n{inverso}')