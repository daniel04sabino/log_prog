#senha
senha= int(input('Digite sua senha: '))
while senha<1000 or senha >9999:
    senha= int(input('Digite sua senha: '))
print('senha PIN aceita!\n\n ')

def inicializarSistema():
    for i in range (5,0,-1):
        print(f'{i}...')
    print('Sistema inicializado com sucesso! ')




confirmacao_senha=int(input('Para entrar no sistema, digite o PIN'))
acesso_liberado=(False)
tentativa=3
while tentativa>0:
    if confirmacao_senha!=senha:
        confirmacao_senha=int(input(f'Senha errada, digite o PIN corretamente\nVocê ainda tem {tentativa} disponíveis: '))
        tentativa-=1

    elif confirmacao_senha == senha:
        inicializarSistema()
        # acesso_liberado=(True)
        break
    
    else:
        print('Conta Bloqueada')
        
    
if acesso_liberado:
    print('Teste')
    for i in range (5,0,-1):
        print(f'{i}...')
    print()
