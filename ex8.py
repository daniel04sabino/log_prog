# Exercício 8: Gestão de Ponto de Reposição de Estoque
# Construa um sistema de controle de reposição para almoxarifado utilizando vetores
# unidimensionais para gerenciar 6 itens industriais.
# ● Regras de Negócio e Requisitos:
# 1. O programa deve preencher duas listas paralelas de tamanho fixo (6 posições): uma contendo o
#  código numérico de cada produto e outra contendo o respectivo saldo em estoque.
# 2. Solicite ao operador o valor do "Estoque Mínimo de Segurança" (um
# número inteiro único para a verificação de toda a linha).
# 3. Realize uma varredura nas estruturas e identifique:
# Quais produtos estão com saldo estritamente abaixo do estoque mínimo,exibindo seu código e quant 
# atual; O código e a quantidade do item que possui o menor saldo
# absoluto no almoxarifado;
# ■ O código e a quantidade do item com maior saldo absoluto.
# 4. Caso nenhum produto esteja abaixo do estoque de segurança, exiba a
# mensagem "Estoque Operando em Parâmetros Normais".
# ● Restrição Técnica: Utilize laços de repetição (for ou while) com controle de
# índices para percorrer as listas de forma sincronizada.
cod_numerico=[]
saldo_estoque=[]

for i in range(6):
    codigo = int(input('Digite o codigo numerico do produto: '))
    saldo = int(input('Digite o saldo desse produto: '))

    cod_numerico.append(codigo)
    saldo_estoque.append(saldo)

estoque_minimo = int(input('Informe o valor mínimo de estoque: '))
indice_menor=0
indice_maior=0
# for codigo, saldo in cod_numerico,saldo_estoque: || Pythones
for i in range(6):
    if saldo_estoque[i]<estoque_minimo:
        print(f'Código {cod_numerico[i]} - Saldo Atual {saldo_estoque[i]}.')
    if saldo_estoque[i]> saldo_estoque[indice_maior]:
        indice_maior=i
    if saldo_estoque[i]> saldo_estoque[indice_menor]:
            indice_menor=i

print(f'O maior {indice_maior}')
# menor=min(saldo_estoque)
# maior=max(saldo_estoque)
# indice1=cod_numerico
    