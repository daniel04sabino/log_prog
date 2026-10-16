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


voltar =True
def banco_de_candidatos(nom,idad,tel,emai,graduasao):
    while voltar:
        nom= input('Digite seu nome: ')
        idad= int(input('Digite sua idade: '))
        if idad<18:
            print('Voce não tem idade suficiente.')
            nom=None
            voltar=False
        elif idad>18:
            tel= int(input('Digite seu número de telefone: \nApenas os números com o DD\n'))
            emai=input('Digite seu email')
            graduasao=input('Digite sua formação')
            candidato={
            'nome': nom,
            'idade': idad,
            'telefone': tel,
            'email': emai,
            'graduacao': graduasao
            }
            banco_candidatos.append(candidato)

prog=int(input('Digite 0 para continuar registrando ou 1 para encerrar: '))
while prog !=0 or prog!=1:
    prog=int(input('Digite 0 para continuar registrando ou 1 para encerrar: '))
    if prog==0:
        voltar=True
    elif prog==1:
        print('Tchauu')
        break


banco_candidatos = []


def cadastrar_candidatos():
    for i in range(0, 5):
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))

        if idade < 18:
            print('Você não tem idade suficiente.')
            cadastrar_candidatos()
            

        tel = input('Digite seu número de telefone:\nApenas números com DDD: ')
        email = input('Digite seu email: ')
        graduacao = input('Digite sua formação: ')

        candidato = {
            'nome': nome,
            'idade': idade,
            'telefone': tel,
            'email': email,
            'graduacao': graduacao
        }

        banco_candidatos.append(candidato)


def mostrar_candidatos():
    for candidato in banco_candidatos:
        print(
            f"Nome: {candidato['nome']} | "
            f"Email: {candidato['email']} | "
            f"Formação: {candidato['graduacao']}"
        )


cadastrar_candidatos()
mostrar_candidatos()