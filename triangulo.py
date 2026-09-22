l1 = float (input("Digite o primeiro lado: "))
l2 = float (input("Digite o segundo lado: "))
l3 = float (input("Digite o ultimo lado: "))
# if l1 ==0 or l2==0 or l3==0:
#     print("Erro!")

condicao= l1 + l2 >l3 and l1+l3>l2 and l2+l3 >l1
condicao2= l1 ==l2 or l2==l3 or l1 ==l3
diferente= l1 != l2 and l1!=l3 and l2!=l3
if not condicao:
    print("Erro!")

elif l1==l2 and l2==l3:
    print('O triângulo é Equilátero. ')
elif condicao2:
    print("O triângulo é Isósceles. ")

elif diferente:
    print("O triângulo é Escaleno. ")
