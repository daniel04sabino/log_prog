nota=float(input('digite sua nota: '))
# notas=[0,1,2,3,4,5,6,7,8,9,10]

while(nota<0 or nota>10):
 print(f'Você digitou {nota}. ')
 nota=float(input('digite sua nota entre 0 e 10. '))