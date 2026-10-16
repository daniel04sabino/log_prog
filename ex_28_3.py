# 7: Processamento de Ponto de Venda - PDV
# O catálogo de preços de um e-commerce é estruturado como um dicionário onde a
# chave é o código de barras (string) e o valor é uma tupla (nome_produto,
# preco_unitario):

# Uma venda foi registrada com a seguinte lista de itens solicitados (código e
# quantidade comprada):

# Escreva um algoritmo que:
# 1. Itere sobre a lista carrinho.
# 2. Localize cada item no catalogo via chave.
# 3. Calcule o subtotal de cada produto (preco_unitario * qtd) e o total geral da
# venda.
# 4. Exiba no terminal um cupom fiscal simplificado: Nome do produto,
# quantidade, preço unitário, subtotal e, ao final, o valor total do pedido.

catalogo={
    '7891001': ('Teclado Mecânico',250.00),
    '7891002': ('Mouse Óptico', 85.50),
    '7891003': ('Monitor 24 Pol', 890.00),
    '7891004': ('Headset USB', 175.20)
}

carrinho=[
    {'codigo': '7891001', 'qtd': 2},
    {'codigo': '7891003', 'qtd': 1},
    {'codigo': '7891004', 'qtd': 3}
]
soma=0
for iten in carrinho:
    if iten['qtd']>1:
        som=iten['qtd']*catalogo[carrinho['codigo']]
        soma+=som
    else:
        print(iten)
    soma+=catalogo[iten['codigo']]

print(soma)