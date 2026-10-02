# Construa uma página/programa onde o usuário digitará o nome e o bairro de
# dez pessoas. O programa exibirá o nome e bairro das pessoas em ordem
# alfabética.

# OK Codiguinho ok

lista = []
for i in range(0, 10):
    nome = input('Digite o seu nome: ')
    bairro = (input('Digite seu bairro: '))
    lista.append([nome, bairro])

lista.sort(key=lambda x: x[1])

# lista.sort = lista[0][1]
print(lista)


