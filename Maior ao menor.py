n1= int(input("Digite o primeiro número"))
n2= int(input("Digite o segundo número"))
n3= int(input("Digite o ultimo número"))

# if n1 > n2 and n3 :

# n1 n2 n3

if n1>n2 and n2>n3:
 print(f"O maior número é {n1}, o do meio é {n2}, e o menor é {n3}. ")
# n1 n3 n2
elif n1>n3 and n3>n2:
 print(f"O maior número é {n1}, o do meio é {n3}, e o menor é {n2}. ")

# n2 n1 n3
elif n2>n1 and n1>n3:
 print(f"O maior número é {n2}, o do meio é {n1}, e o menor é {n3}. ")
# n2 n3 n1
elif n2>n3 and n3>n1:
 print(f"O maior número é {n2}, o do meio é {n3}, e o menor é {n1}. ")

# n3 n1 n2
elif n3>n1 and n1>n2:
 print(f"O maior número é {n3}, o do meio é {n1}, e o menor é {n2}. ")
# n3 n2 n1
elif n3>n2 and n2>n1:
 print(f"O maior número é {n3}, o do meio é {n2}, e o menor é {n1}. ") 
 
print(f"O N1 é {n1}, o N2 é {n2} e o n3 é {n3}. ")