# Crie uma função chamada registrar_acesso(usuario) que recebe o nome de
# um usuário e anexa esse registro no arquivo acessos.log.
# a. se o arquivo não existir, o Python deve criá-lo;
# b. se já existir, as novas informações devem ser inseridas no final, preservando o
# histórico existente.

def registro_de_acesso(usuario):
    with open('Senai.log' , 'a' , encoding='utf-8') as arquivo:
        arquivo.write(usuario+'\n')

while True:
    user= input('Digite nome de usuário: ')
    registro_de_acesso(user)
    if user=='0':
        break