numeros=[]
i=1
start=(False)
for i in range(0,8):
    numero= int(input('Digite um número: '))
    numeros.append(numero)

x=int(input('Digite um número para saber se tenho no meu Banco e a posição dele: '))

if x in numeros:
    a=numeros.index(x)
    print(f'{a+1}º')
else:
    print(f'O número {x} não está no meu banco. ')