# Aprendendo usar for

# isso é em Java
# for(i=0; i<4; i++){
# }

n1 = int(input('Digite o numero que quer descobrir a tabuada '))
tab=1
# tabuada= n1/i
for i in range (0 ,10):
    # print(i)
  
    
    tabuada= n1*tab
    print(f"tabuada de {n1} X {tab} é = {tabuada} " )
    tab+=1

# pular 2 em 2 
# for b in range(1,20,2):
#     print(b)

# cs=['carro','moto','caminhão','fone']

# for yc in cs:
#     print(yc) 