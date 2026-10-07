
# Desenvolva um módulo de console para auditar o consumo de combustível de
# veículos que retornam à base operacional ao longo de um turno de trabalho.
# ● Regras de Negócio e Requisitos:
# 1. O programa deve processar múltiplos veículos de forma contínua até
# que o operador digite 0 na quilometragem percorrida para sinalizar o
# fim do expediente.
# 2. Para cada veículo válido, solicite a distância percorrida (em km) e a
# quantidade de combustível consumida (em litros). Utilize um laço while
# para validar que o volume de combustível seja estritamente maior que
# zero antes de prosseguir com o cálculo.
# 3. Calcule o consumo médio (km/l) e classifique o desempenho do
# veículo:
# ■ Consumo maior ou igual a 12. 0km/l: "Econômico";
# ■ Consumo entre 9. 0km/l e 11. 9km/l: "Padrão";
# ■ Consumo inferior a 9. 0km/l: "Alto Consumo".
# 4. Exiba a classificação do veículo processado.
# 5. Ao encerrar o expediente, exiba:
# ■ O total de veículos auditados;
# ■ A quilometragem total acumulada pela frota;
# ■ A média geral de consumo da frota no turno.
# ● Restrição Técnica: O processamento deve utilizar unicamente
# acumuladores e variáveis numéricas primitivas (float e int), sem o uso de
# listas ou estruturas compostas.
total_quilomentragem=0
total_consumo=0
veiculos=0



while True:
    km_rodados=float(input('Digite os km rodados do veiculo: '))
    if km_rodados==0 :
            break
    else:
        consumo=float(input('Digite os gastos com combustível do veiculo: '))
        total_quilomentragem +=km_rodados
        total_consumo +=consumo
        veiculos+=1

        consumo2=km_rodados/consumo

        if consumo2 < 9:
            print('Alto consumo')
        elif consumo2>=9 and consumo2<12:
            print('Padrão')
        else:
            print('Econômico')



print(f'quantidade de veiculos: {veiculos}\nTotal km rodado: {total_quilomentragem} | Total de consumo: {total_consumo}')

