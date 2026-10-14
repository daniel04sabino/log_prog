dict

produto={
    'sku': 'MEM-16GB',
    'nome': 'Memória RAM DDR5',
    'preco': 1100.00,
    'quantidade': 15,
    'ativo': True
}
# print(produto)
produto['preco'] = produto['preco']*1.1
produto['quantidade']=8
# print(produto)
print(f'Produto: {produto['nome']} | valor: {produto['preco']}')

for chave,valor in produto.items():
    print(f'{chave}: {valor}')