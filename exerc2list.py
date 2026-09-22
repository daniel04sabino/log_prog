impar=[]
par=[]
for i in range(0,7):
    numero= int(input('Digite um número: '))
    if (numero%2)==0:
        par.append(numero)
    else:
        impar.append(numero)
print(f'Os números impar são: {impar}\n Os Números pares são: {par}')