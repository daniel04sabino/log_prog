# Aluno: Daniel Rocha Sabino

# 4. Auditoria de Eficiência Energética de Linha Industrial
# a. Desenvolva um sistema de console para auditar o consumo elétrico de maquinários em uma
# linha de produção industrial. O sistema deve monitorar 5 máquinas utilizando vetores
# unidimensionais.
# i. Regras de Negócio e Requisitos:
# 1. O programa deve preencher duas listas paralelas de tamanho fixo (5
# posições): uma contendo o código numérico de identificação de cada

# máquina e outra contendo o respectivo consumo registrado em quilowatt-
# hora (kWh).
# 2. Para cada máquina, o sistema deve validar a entrada do consumo através de
# um laço while, garantindo que o valor informado em kWh seja estritamente
# maior que zero antes de passar para a máquina seguinte.
# 3. Solicite ao operador o valor do "Teto Operacional de Consumo" (número real
# único para a verificação de toda a linha industrial).
# 4. Realize uma varredura nas estruturas e identifique:
# a. Quais máquinas ultrapassaram o teto operacional, exibindo seu
# código e o consumo registrado;
# b. O código e o consumo da máquina com o maior consumo absoluto da
# planta;
# c. A média aritmética de consumo de todas as 5 máquinas.
# 5. Caso nenhuma máquina tenha ultrapassado o teto operacional, o programa
# deve exibir a mensagem: "Operação Dentro dos Parâmetros de Eficiência".
# ii. Restrição Técnica: Utilize laços de repetição (for ou while) com controle explícito de
# índices para percorrer as listas de forma sincronizada. É vedado o uso de funções
# prontas da linguagem para busca (como max(), min()), devendo a identificação de
# extremos e acumulações ser realizada puramente por lógica de varredura e variáveis
# de controle. É vedado o uso de estruturas não vistas em sala.

# preciso de uma matriz [
#     [maquina,consumo kwh]
# ]
# while para kwh  que não pode ser 0
# teto operacional (limite de consumo)
# mostrar quais passaram do teto exibindo codigo e consumo
# consumo das 5
# se não passar do teto deve exibir a mensagem: "Operação Dentro dos Parâmetros de Eficiência".
# e função
import copy#evitar erro com copiar
#lista e soma de todos
maquinario=[]
total=float()
#loop para receber o id e consumo da máquina e somando cada um dando um loop caso o consumo seja menor ou igual a 0
for i in range(0,5):
    id=input('Digite código da máquina:\nExemplo:M001: ')
    consumo=float(input(f'Digite o consumo em KWh da máquina {id}: '))
    while consumo<=0:
        consumo=float(input(f'Digite o consumo em KWh da máquina {id}: '))
    
    total+=consumo
    maquinario.append([id,consumo])



teto_operacional=float(input('Digite o teto operacional: '))
contador2=0#para saber se 1 ultrapassou o limite do teto

indice_menor = 0
indice_maior = 0
contador = 0
for i in range(6):
    #achar o maior
    if consumo[i] < teto_operacional:
        contador += 1
    if consumo[i] > teto_operacional[indice_maior]:
        indice_maior = i

  
#loop para mostrar as máquinas
for i in range(len(maquinario)):
    print(f'Máquina: {maquinario[i][0]} | Consumo em KWh: {maquinario[i][1]}')
    if maquinario[i][1] > teto_operacional:
        print('Alto Consumo\n')
        contador+=1
        print(60*'-')
    else:
        print(60*'-')
#maior consumo,total e se todos estiverem abaixo do teto
print(f'A máquina com maior consumo foi {maquinario[indice_maior][0]} e seu consumo foi: {maquinario[indice_maior][1]}')
print(f'O gasto total do dia foi: {total}')
if contador2==0:
    print('Operação Dentro dos Parâmetros de Eficiência.')