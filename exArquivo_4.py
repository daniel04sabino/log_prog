# Criar um script em Python que leia o arquivo vendas_bruto.csv, aplique cálculos e
# regras de negócio para cada pedido e gere um novo arquivo chamado
# faturamento_consolidado.csv.
# a. Para cada linha do arquivo, realize as seguintes operações:
# i. Valor Bruto: quantidade * preco_unitario
# ii. Desconto: 10% do valor bruto se a quantidade >= 5; caso contrário, 0.00
# iii. Valor Líquido: valor_bruto - desconto
# iv. Status: "PREMIUM" se valor_liquido >= 1000.00; caso contrário, "PADRAO"
import csv
# id_pedido;cliente;produto;quantidade;preco_unitario;categoria
with open('vendas.csv' , 'r'  ,encoding='utf-8') as f:
    leitor= csv.DictReader(f, delimiter=';')
    for item in leitor: 
        # print(item)
        

        valor= float(item['preco_unitario'])
        quant= float(item['quantidade'])
        desconto=0
        valorBruto=valor * quant
        if quant>=5:
            desconto=valorBruto*0.10

        liquido= valorBruto-desconto
        if liquido>=1000.00:
            status='PREMIUM'
        else:
            status='PADRAO'
        print(liquido)
        print(status)
            
        print(valorBruto)








        # conteudo=linha.strip()
        # valorBruto=linha['quantidade']*linha['preco_unitario']
        # if linha['quantidade'] >=5:
        #     desconto+= valorBruto*0,10


        # valor_liquido=valorBruto-desconto
        # print(f'{valorBruto} e {desconto} e {valor_liquido}')
        # # print(conteudo)