nome=input('Digite seu nome: ')
cidade=input('Digite sua cidade: ')

def vereficar_local(nome,cidade):
    if cidade =='Rio de Janeiro' or cidade=='RJ':
        print(f'Olá {nome}.\nSeja bem-vindo a Cidade Maravilhosa! ')
    else:
        print(f'Olá {nome}.\nSeja bem-vindo a {cidade}! ')
   
vereficar_local(nome,cidade)

# print(vereficar_local)
