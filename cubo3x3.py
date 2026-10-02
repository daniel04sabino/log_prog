#Matriz||Cubo 3X3
matriz=[]
for i in range (3):
    linha=[]
    for j in range(3):
        numero=int(input('Digite um número entre 1 e 9: '))
        while numero<1 or numero>9:
            numero=int(input('Digite um número entre 1 e 9: '))
        
        linha.append(numero)
    
    matriz.append(linha)
#validar as linhas
valores=[]
for i in range (3):
    for j in range (3):
        valores=matriz[i][j]

valores_ordenados= sorted(valores)
valores_validos = valores_ordenados== list(range(1,10))

soma =0
somas=[]
for linha in matriz:
    for numero in linha:
        soma +=numero
        somas.apend(soma)

#ainda falta

#Versão2
