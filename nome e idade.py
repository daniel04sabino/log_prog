
# OK codiginho rodando ok

lista = []
for i in range(0, 4):
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite sua idade: '))
    lista.append([nome, idade])

mais_novo= 0
for i in range(1,len(lista)):
    if lista[i][1]<lista[mais_novo][1]:
        mais_novo=i
        

print(f'{lista[mais_novo]}')