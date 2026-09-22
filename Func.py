# Somar

# def somar(a, b):
#     a=a+b
#     return a
# a=5
# b=4
# c = somar(b,a)
# print(c)
# print(a)

# Subtrair
def subtrair(a,b):
    '''
    Essa função subtrair o 'a' de 'b' e retorna o valor '''
    return a-b
subtrair(1,1)
#saber se é impar
def impar(numero):
    if not numero % 2 ==0:
        return True
    return False

def vereficar_senha(senha):
    '''
    Descobri se tem 8 digitos na senha
    '''
    return len(senha)>=8