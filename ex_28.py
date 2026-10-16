# 5: Módulo de Triagem de Recrutamento
# Desenvolva um programa que simule a coleta e armazenamento de dados de 5
# candidatos a vagas de emprego:
# ● Cada candidato deve ser representado por um dicionário com os campos:
# "nome", "idade", "telefone", "email" e "formacao".

# ● Todos os candidatos aprovados na triagem devem ser armazenados em uma
# lista principal chamada banco_candidatos.

# ● Regra de negócio: Candidatos com idade inferior a 18 anos não podem
# participar do processo. Caso a idade informada seja menor que 18, o
# programa deve rejeitar o registro, exibir uma mensagem de recusa e não
# inserir o candidato na lista.

# ● Ao término da entrada de dados, o sistema deve iterar sobre
# banco_candidatos e exibir um relatório contendo: Nome, E-mail e Formação
# de cada candidato apto.
banco_candidatos=[]



for i in range(0,5):
    nome= input('Digite seu nome: ')
    idade= int(input('Digite sua idade: '))
    if idade>=18:
            tel= int(input('Digite seu número de telefone: \nApenas os números com o DDD\n: '))
            email=input('Digite seu email: ')
            graduacao=input('Digite sua formação: ')
            candidato={
            'nome': nome,
            'idade': idade,
            'telefone': tel,
            'email': email,
            'graduacao': graduacao
            }
            banco_candidatos.append(candidato)
    elif idade<18:
        print('Voce não tem idade suficiente.')
        pass
        
    
for i in range(len(banco_candidatos)):
    print(f'nome: {banco_candidatos[i]['nome']} | Email: {banco_candidatos[i]['email']} | Formação: {banco_candidatos[i]['graduacao']}')






     
# # prog=int(input('Digite 0 para continuar registrando ou 1 para encerrar: '))
# # while prog !=0 or prog!=1:
# #     prog=int(input('Digite 0 para continuar registrando ou 1 para encerrar: '))
# #     if prog==0:
# #         voltar=True
# #     elif prog==1:
# #         print('Tchauu')
# #         break
