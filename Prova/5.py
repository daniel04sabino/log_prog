# Aluno: Daniel Rocha Sabino

# Desenvolva um módulo de console para auditar a temperatura de operação de servidores
# organizados em um rack de data center. O sistema deve gerenciar uma matriz 3x3, onde cada
# linha representa um rack físico (Rack 0, Rack 1 e Rack 2) e cada coluna representa um sensor
# de temperatura instalado (Sensor 0, Sensor 1 e Sensor 2).
# i. Regras de Negócio e Requisitos:
# 1. O programa deve preencher a matriz 33 com as temperaturas registradas em
# graus Celsius (valores do tipo float).
# 2. Utilize um laço while para validar individualmente a entrada de cada sensor,
# aceitando apenas temperaturas contidas na faixa operacional entre 10.0C e
# 90.0C.
# 3. Para cada um dos três racks (linhas da matriz), o programa deve calcular e
# exibir a temperatura média dos sensores que o compõem.
# 4. Identifique o ponto crítico da estrutura: descubra a maior temperatura
# absoluta registrada em toda a matriz e exiba o seu valor juntamente com as
# coordenadas exatas da sua localização (número do rack/linha e número do
# sensor/coluna).
# 5. Imprima a matriz completa formatada em linhas e colunas.
# 6. Caso a maior temperatura absoluta encontrada seja igual ou superior a 75.0C,
# exiba uma mensagem de "ALERTA: Ponto Crítico de Sobreaquecimento
# Detectado".
# ii. Restrição Técnica: A manipulação da matriz bidimensional deve ser realizada por
# meio de laços for aninhados. É proibida a utilização de funções prontas de biblioteca
# ou funções nativas de buscas (como max(), min()), sendo obrigatória a
# implementação manual de acumuladores e controle condicional de extremos. É
# vedado o uso de estruturas não vistas em sala.

#loop para salvar a temperatura
matriz=[]  #3x3
for coluna in range(0,3):
    coluna=[]
    for linha in range(0,3):
        temperatura=float(input('Digite a temperatura: '))
        while 10.0>temperatura<90.0:
            temperatura=float(input('Digite a temperatura: '))

        coluna.append(temperatura)
    matriz.append(coluna)
# media_geral=[]

alerta=75.0


# descobrir o maior
indice_menor = 0
indice_maior = 0
contador = 0
for i in range(6):
    
    # if matriz[i] < matriz[]:
    #     contador += 1
    if matriz[i] > matriz[indice_maior]:
        indice_maior = i
    # achar o menor - verifica se a posição da lista tem menor quantidade do
    # que o menor anterior
    if matriz[i] < matriz[indice_menor]:
        indice_menor = i

#mostrar todos
for i in range(len(matriz)):
    print(f'Rack: {linha[i]} | Temperatura: {matriz[i][1]}')
    print(60*'-')
#alerta da temperatura alta
for i in matriz:
    for temp in i:
        if matriz[i][temp]<=alerta:
            print(f'ALERTA: Ponto Crítico de Sobreaquecimento Detectado.')

