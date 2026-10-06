# Implemente um programa que receba as temperaturas médias registradas durante
# os 7 dias da semana (armazenadas em um vetor de números reais). O programa
# deve calcular a média aritmética semanal e, em seguida, exibir quais temperaturas
# registradas ficaram estritamente abaixo dessa média.

print('De olho na meteorologia.\n')
week=[]
for dia in range(0,3):
    data= input('digite a data:\nExemplo:01/02/2026\n ')
    dia_da_semana= input('Digite o dia da semana:\nExemplos:Seg,Ter,Qua,Qui,Sex,Sab e Dom.\n')
    temperatura= int(input(f'Digite a temperatura do dia {data}:\nApenas o número: '))
    week.append([data,dia_da_semana,temperatura])
# print(week)
soma=int()
quant=len(week)
for i in range(len(week)):
    soma+=week[i][2]


media=soma/quant

print(f'A temperatura média dessa semana foi: {media}ºC')
for dia in week:
    print(f'A temperatura em cada dia da semana foi:\n{dia[1]} |Temperatura: {dia[2]}')
