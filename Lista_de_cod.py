def impar(numero):
    if not numero % 2 ==0:
        return True
    return False

def vereficar_senha(senha):
    '''
    Descobri se tem 8 digitos na senha
    '''
    return len(senha)>=8