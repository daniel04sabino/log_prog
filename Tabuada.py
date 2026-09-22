print("Vamos aprender a tabuada? ")
numero= int(input("Digite a tabuada que quer aprender. "))
n_loop= 1
# tabuada=numero*n_loop
print(f"tabuada do número {numero} é:\n ")
while n_loop<=10:
    tabuada=numero*n_loop
    print(f"{numero}  X {n_loop}= {tabuada}")
    n_loop+=1
